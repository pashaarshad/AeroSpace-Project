import React from 'react';

const About = () => {
  return (
    <div className="max-w-4xl mx-auto">
      <div className="bg-white rounded-lg shadow-lg overflow-hidden">
        {/* Hero Section */}
        <div className="bg-gradient-to-r from-indigo-600 to-purple-600 text-white px-8 py-12">
          <h1 className="text-4xl font-bold mb-4">About DeepBot</h1>
          <p className="text-xl text-indigo-100">
            Revolutionizing knowledge discovery with AI-powered graph intelligence
          </p>
        </div>

        {/* Main Content */}
        <div className="p-8">
          <div className="prose max-w-none">
            <h2 className="text-2xl font-bold text-gray-900 mb-4">What is DeepBot?</h2>
            <p className="text-gray-600 mb-6">
              DeepBot is an advanced AI-powered knowledge retrieval system that transforms how you interact with information. 
              By combining cutting-edge natural language processing with dynamic knowledge graphs, DeepBot creates an 
              intelligent ecosystem where your documents, research papers, and data sources come alive through interactive 
              visualizations and conversational AI.
            </p>

            <h2 className="text-2xl font-bold text-gray-900 mb-4">Key Features</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
              <div className="bg-blue-50 p-6 rounded-lg">
                <h3 className="font-semibold text-blue-900 mb-2">🤖 AI Chat Interface</h3>
                <p className="text-blue-800 text-sm">
                  Engage in natural conversations with your knowledge base. Ask complex questions and receive 
                  contextual answers backed by your documents and scholarly sources.
                </p>
              </div>
              <div className="bg-green-50 p-6 rounded-lg">
                <h3 className="font-semibold text-green-900 mb-2">🕸️ Dynamic Knowledge Graphs</h3>
                <p className="text-green-800 text-sm">
                  Visualize complex relationships between concepts, entities, and ideas through interactive 
                  graph visualizations powered by Neo4j and D3.js.
                </p>
              </div>
              <div className="bg-purple-50 p-6 rounded-lg">
                <h3 className="font-semibold text-purple-900 mb-2">📄 Smart Document Processing</h3>
                <p className="text-purple-800 text-sm">
                  Upload documents in various formats and watch as DeepBot automatically extracts entities, 
                  relationships, and key concepts to expand your knowledge graph.
                </p>
              </div>
              <div className="bg-orange-50 p-6 rounded-lg">
                <h3 className="font-semibold text-orange-900 mb-2">🔍 Scholarly Integration</h3>
                <p className="text-orange-800 text-sm">
                  Seamlessly integrate with academic databases and research repositories to enrich your 
                  knowledge base with authoritative sources.
                </p>
              </div>
            </div>

            <h2 className="text-2xl font-bold text-gray-900 mb-4">Technology Stack</h2>
            <div className="bg-gray-50 p-6 rounded-lg mb-6">
              <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div>
                  <h4 className="font-semibold text-gray-900 mb-2">Frontend</h4>
                  <ul className="text-sm text-gray-600 space-y-1">
                    <li>• React 18+ with Hooks</li>
                    <li>• Vite for fast development</li>
                    <li>• Tailwind CSS for styling</li>
                    <li>• D3.js for visualizations</li>
                    <li>• React Router for navigation</li>
                  </ul>
                </div>
                <div>
                  <h4 className="font-semibold text-gray-900 mb-2">Backend</h4>
                  <ul className="text-sm text-gray-600 space-y-1">
                    <li>• Flask REST API</li>
                    <li>• Neo4j Graph Database</li>
                    <li>• LangChain for LLM integration</li>
                    <li>• spaCy for NLP processing</li>
                    <li>• LlamaIndex for RAG</li>
                  </ul>
                </div>
                <div>
                  <h4 className="font-semibold text-gray-900 mb-2">AI & ML</h4>
                  <ul className="text-sm text-gray-600 space-y-1">
                    <li>• OpenRouter for LLM access</li>
                    <li>• DeepSafe for AI safety</li>
                    <li>• HuggingFace Transformers</li>
                    <li>• Sentence Transformers</li>
                    <li>• Custom NER models</li>
                  </ul>
                </div>
              </div>
            </div>

            <h2 className="text-2xl font-bold text-gray-900 mb-4">How It Works</h2>
            <div className="space-y-4 mb-6">
              <div className="flex items-start space-x-4">
                <div className="w-8 h-8 bg-blue-600 text-white rounded-full flex items-center justify-center text-sm font-semibold">1</div>
                <div>
                  <h4 className="font-semibold text-gray-900">Document Ingestion</h4>
                  <p className="text-gray-600 text-sm">Upload your documents, research papers, or connect to data sources</p>
                </div>
              </div>
              <div className="flex items-start space-x-4">
                <div className="w-8 h-8 bg-blue-600 text-white rounded-full flex items-center justify-center text-sm font-semibold">2</div>
                <div>
                  <h4 className="font-semibold text-gray-900">AI Processing</h4>
                  <p className="text-gray-600 text-sm">Our NLP pipeline extracts entities, relationships, and concepts</p>
                </div>
              </div>
              <div className="flex items-start space-x-4">
                <div className="w-8 h-8 bg-blue-600 text-white rounded-full flex items-center justify-center text-sm font-semibold">3</div>
                <div>
                  <h4 className="font-semibold text-gray-900">Graph Construction</h4>
                  <p className="text-gray-600 text-sm">Knowledge graphs are built and stored in Neo4j for fast querying</p>
                </div>
              </div>
              <div className="flex items-start space-x-4">
                <div className="w-8 h-8 bg-blue-600 text-white rounded-full flex items-center justify-center text-sm font-semibold">4</div>
                <div>
                  <h4 className="font-semibold text-gray-900">Interactive Exploration</h4>
                  <p className="text-gray-600 text-sm">Chat with your knowledge base or explore visual graph representations</p>
                </div>
              </div>
            </div>

            <h2 className="text-2xl font-bold text-gray-900 mb-4">Getting Started</h2>
            <div className="bg-blue-50 p-6 rounded-lg">
              <ol className="text-sm text-blue-800 space-y-2">
                <li><strong>1.</strong> Start by uploading your first document or connecting to a data source</li>
                <li><strong>2.</strong> Watch as DeepBot processes and creates your knowledge graph</li>
                <li><strong>3.</strong> Begin chatting with your AI assistant to explore your knowledge base</li>
                <li><strong>4.</strong> Use the graph visualization to discover new connections and insights</li>
                <li><strong>5.</strong> Continuously add more sources to expand your knowledge ecosystem</li>
              </ol>
            </div>
          </div>
        </div>

        {/* Footer CTA */}
        <div className="bg-gray-50 px-8 py-6 text-center">
          <h3 className="text-lg font-semibold text-gray-900 mb-2">Ready to get started?</h3>
          <p className="text-gray-600 mb-4">Transform your information into intelligent knowledge graphs today.</p>
          <button className="bg-blue-600 text-white px-6 py-3 rounded-lg font-medium hover:bg-blue-700 transition-colors">
            Start Building Your Knowledge Graph
          </button>
        </div>
      </div>
    </div>
  );
};

export default About;
