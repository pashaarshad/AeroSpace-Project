from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import requests
import json
from datetime import datetime
import logging
from knowledge_graph import KnowledgeGraph
from document_processor import DocumentProcessor
from ai_safety import DeepSafeValidator
from scholarly_search import ScholarlySearch

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize components
kg = KnowledgeGraph()
doc_processor = DocumentProcessor()
safety_validator = DeepSafeValidator()
scholarly_search = ScholarlySearch()

# Configuration
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
DEEPSAFE_API_KEY = os.getenv('DEEPSAFE_API_KEY')
NEO4J_URI = os.getenv('NEO4J_URI')
NEO4J_USER = os.getenv('NEO4J_USER')
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    """Main chat endpoint for AI interactions"""
    try:
        data = request.get_json()
        user_query = data.get('query', '').strip()
        
        if not user_query:
            return jsonify({'error': 'Query is required'}), 400
        
        # Step 1: Safety validation
        safety_check = safety_validator.validate_query(user_query)
        if not safety_check['is_safe']:
            return jsonify({
                'error': 'Query failed safety validation',
                'reason': safety_check['reason']
            }), 400
        
        # Step 2: Knowledge Graph search
        kg_results = kg.search_knowledge(user_query)
        
        # Step 3: Document search
        doc_results = doc_processor.search_documents(user_query)
        
        # Step 4: Scholarly search (if needed)
        scholarly_results = []
        if data.get('include_scholarly', False):
            scholarly_results = scholarly_search.search_papers(user_query)
        
        # Step 5: Generate AI response
        ai_response = generate_ai_response(
            user_query, 
            kg_results, 
            doc_results, 
            scholarly_results
        )
        
        return jsonify({
            'response': ai_response,
            'sources': {
                'knowledge_graph': kg_results,
                'documents': doc_results,
                'scholarly': scholarly_results
            },
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        logger.error(f"Chat endpoint error: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/knowledge-graph', methods=['GET'])
def get_knowledge_graph():
    """Get knowledge graph data for visualization"""
    try:
        graph_data = kg.get_graph_data()
        return jsonify(graph_data)
    except Exception as e:
        logger.error(f"Knowledge graph endpoint error: {str(e)}")
        return jsonify({'error': 'Failed to retrieve graph data'}), 500

@app.route('/api/upload-document', methods=['POST'])
def upload_document():
    """Upload and process new documents"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Process the document
        result = doc_processor.process_uploaded_file(file)
        
        # Update knowledge graph
        kg.update_from_document(result)
        
        return jsonify({
            'message': 'Document processed successfully',
            'entities_extracted': result['entities_count'],
            'relations_extracted': result['relations_count']
        })
        
    except Exception as e:
        logger.error(f"Document upload error: {str(e)}")
        return jsonify({'error': 'Failed to process document'}), 500

@app.route('/api/search-papers', methods=['POST'])
def search_papers():
    """Search for academic papers"""
    try:
        data = request.get_json()
        query = data.get('query', '')
        limit = data.get('limit', 10)
        
        papers = scholarly_search.search_papers(query, limit)
        
        return jsonify({
            'papers': papers,
            'count': len(papers),
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        logger.error(f"Paper search error: {str(e)}")
        return jsonify({'error': 'Failed to search papers'}), 500

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get system statistics"""
    try:
        stats = {
            'knowledge_graph': kg.get_stats(),
            'documents': doc_processor.get_stats(),
            'system': {
                'uptime': datetime.now().isoformat(),
                'version': '1.0.0'
            }
        }
        return jsonify(stats)
    except Exception as e:
        logger.error(f"Stats endpoint error: {str(e)}")
        return jsonify({'error': 'Failed to retrieve stats'}), 500

@app.route('/ask', methods=['POST'])
def ask():
    """Handle AI-based queries"""
    try:
        data = request.json
        query = data.get('query', '')
        
        # Placeholder for AI response logic
        response = {
            "answer": f"You asked: {query}. This is a placeholder response."
        }
        
        return jsonify(response)
    
    except Exception as e:
        logger.error(f"Ask endpoint error: {str(e)}")
        return jsonify({'error': 'Failed to process request'}), 500

def generate_ai_response(query, kg_results, doc_results, scholarly_results):
    """Generate AI response using OpenRouter"""
    try:
        # Prepare context from all sources
        context = prepare_context(kg_results, doc_results, scholarly_results)
        
        # Create prompt
        prompt = f"""
        You are an intelligent help bot with access to a knowledge graph and various documents.
        
        User Query: {query}
        
        Context from Knowledge Graph:
        {context['kg_context']}
        
        Context from Documents:
        {context['doc_context']}
        
        Context from Scholarly Sources:
        {context['scholarly_context']}
        
        Please provide a comprehensive, accurate, and helpful response based on the available context.
        If you cannot find relevant information, please say so clearly.
        """
        
        headers = {
            'Authorization': f'Bearer {OPENROUTER_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            'model': 'mistralai/mixtral-8x7b-instruct',
            'messages': [
                {
                    'role': 'user',
                    'content': prompt
                }
            ],
            'max_tokens': 1000,
            'temperature': 0.7
        }
        
        response = requests.post(
            'https://openrouter.ai/api/v1/chat/completions',
            headers=headers,
            json=payload
        )
        
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content']
        else:
            logger.error(f"OpenRouter API error: {response.status_code}")
            return "I apologize, but I'm having trouble generating a response right now."
            
    except Exception as e:
        logger.error(f"AI response generation error: {str(e)}")
        return "I apologize, but I encountered an error while processing your request."

def prepare_context(kg_results, doc_results, scholarly_results):
    """Prepare context from all sources"""
    context = {
        'kg_context': '',
        'doc_context': '',
        'scholarly_context': ''
    }
    
    # Knowledge graph context
    if kg_results:
        context['kg_context'] = '\n'.join([
            f"- {result['entity']}: {result['description']}" 
            for result in kg_results[:5]
        ])
    
    # Document context
    if doc_results:
        context['doc_context'] = '\n'.join([
            f"- {result['title']}: {result['snippet']}" 
            for result in doc_results[:3]
        ])
    
    # Scholarly context
    if scholarly_results:
        context['scholarly_context'] = '\n'.join([
            f"- {paper['title']}: {paper['abstract'][:200]}..." 
            for paper in scholarly_results[:2]
        ])
    
    return context

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
