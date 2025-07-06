import React from 'react';
import { Link } from 'react-router-dom';

const About = () => {
  return (
    <div className="about-page">
      <div className="about-container">
        {/* Hero Section */}
        <div className="about-hero">
          <h1>About DeepBot</h1>
          <p>
            Revolutionizing knowledge discovery with AI-powered graph intelligence
          </p>
        </div>

        {/* Main Content */}
        <div className="about-content">
          <div className="about-section">
            <h2>What is DeepBot?</h2>
            <p>
              DeepBot is an advanced AI-powered knowledge retrieval system that transforms how you interact with information. 
              By combining cutting-edge natural language processing with dynamic knowledge graphs, DeepBot creates an 
              intelligent ecosystem where your documents, research papers, and data sources come alive through interactive 
              visualizations and conversational AI.
            </p>
          </div>

          <div className="about-section">
            <h2>Key Features</h2>
            <div className="features-grid">
              <div className="feature-card blue">
                <h3>🤖 AI Chat Interface</h3>
                <p>
                  Engage in natural conversations with your knowledge base. Ask complex questions and receive 
                  contextual answers backed by your documents and scholarly sources.
                </p>
              </div>
              <div className="feature-card green">
                <h3>🕸️ Dynamic Knowledge Graphs</h3>
                <p>
                  Visualize complex relationships between concepts, entities, and ideas through interactive 
                  graph visualizations powered by Neo4j and D3.js.
                </p>
              </div>
              <div className="feature-card purple">
                <h3>📄 Smart Document Processing</h3>
                <p>
                  Upload documents in various formats and watch as DeepBot automatically extracts entities, 
                  relationships, and key concepts to expand your knowledge graph.
                </p>
              </div>
              <div className="feature-card orange">
                <h3>🔍 Scholarly Integration</h3>
                <p>
                  Seamlessly integrate with academic databases and research repositories to enrich your 
                  knowledge base with authoritative sources.
                </p>
              </div>
            </div>
          </div>

          <div className="about-section">
            <h2>Technology Stack</h2>
            <div className="tech-stack">
              <div className="tech-category">
                <h4>Frontend</h4>
                <ul>
                  <li>React 18+ with Hooks</li>
                  <li>Vite for fast development</li>
                  <li>Custom CSS for styling</li>
                  <li>D3.js for visualizations</li>
                  <li>React Router for navigation</li>
                </ul>
              </div>
              <div className="tech-category">
                <h4>Backend</h4>
                <ul>
                  <li>Flask REST API</li>
                  <li>Neo4j Graph Database</li>
                  <li>LangChain for LLM integration</li>
                  <li>spaCy for NLP processing</li>
                  <li>LlamaIndex for RAG</li>
                </ul>
              </div>
              <div className="tech-category">
                <h4>AI & ML</h4>
                <ul>
                  <li>OpenRouter for LLM access</li>
                  <li>DeepSeek AI Models</li>
                  <li>HuggingFace Transformers</li>
                  <li>Sentence Transformers</li>
                  <li>Custom NER models</li>
                </ul>
              </div>
            </div>
          </div>

          <div className="about-section">
            <h2>How It Works</h2>
            <div className="process-steps">
              <div className="step">
                <div className="step-number">1</div>
                <div className="step-content">
                  <h4>Document Ingestion</h4>
                  <p>Upload your documents, research papers, or connect to data sources</p>
                </div>
              </div>
              <div className="step">
                <div className="step-number">2</div>
                <div className="step-content">
                  <h4>AI Processing</h4>
                  <p>Our NLP pipeline extracts entities, relationships, and concepts</p>
                </div>
              </div>
              <div className="step">
                <div className="step-number">3</div>
                <div className="step-content">
                  <h4>Graph Construction</h4>
                  <p>Knowledge graphs are built and stored in Neo4j for fast querying</p>
                </div>
              </div>
              <div className="step">
                <div className="step-number">4</div>
                <div className="step-content">
                  <h4>Interactive Exploration</h4>
                  <p>Chat with your knowledge base or explore visual graph representations</p>
                </div>
              </div>
            </div>
          </div>

          <div className="about-section">
            <h2>Getting Started</h2>
            <div className="getting-started-guide">
              <div className="guide-steps">
                <div className="guide-step">
                  <span className="guide-number">1</span>
                  <p>Start by uploading your first document or connecting to a data source</p>
                </div>
                <div className="guide-step">
                  <span className="guide-number">2</span>
                  <p>Watch as DeepBot processes and creates your knowledge graph</p>
                </div>
                <div className="guide-step">
                  <span className="guide-number">3</span>
                  <p>Begin chatting with your AI assistant to explore your knowledge base</p>
                </div>
                <div className="guide-step">
                  <span className="guide-number">4</span>
                  <p>Use the graph visualization to discover new connections and insights</p>
                </div>
                <div className="guide-step">
                  <span className="guide-number">5</span>
                  <p>Continuously add more sources to expand your knowledge ecosystem</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Footer CTA */}
        <div className="about-footer">
          <div className="footer-content">
            <h3>Ready to get started?</h3>
            <p>Transform your information into intelligent knowledge graphs today.</p>
            <div className="footer-buttons">
              <Link to="/chat" className="btn-primary">
                Start Chatting Now
              </Link>
              <Link to="/graph" className="btn-secondary">
                Explore Knowledge Graph
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default About;
