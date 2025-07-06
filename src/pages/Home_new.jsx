import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <div className="hero">
        <div className="container">
          <h1 className="text-5xl md:text-6xl font-bold mb-6">
            Welcome to <span className="text-white">DeepBot</span>
          </h1>
          <p className="text-xl mb-8 max-w-3xl mx-auto">
            An AI-powered knowledge retrieval system that creates dynamic knowledge graphs 
            from your documents and scholarly sources. Experience the future of information discovery.
          </p>
          <div className="btn-group">
            <Link to="/chat" className="btn-primary">
              Start Chatting
            </Link>
            <Link to="/graph" className="btn-secondary">
              Explore Graph
            </Link>
          </div>
        </div>
      </div>

      {/* Features Section */}
      <div className="features">
        <div className="container">
          <h2>Powerful Features</h2>
          <p className="features-subtitle">Discover what makes DeepBot unique</p>
          
          <div className="features-grid">
            <div className="feature-card">
              <div className="feature-icon">
                💬
              </div>
              <h3>AI Chat Interface</h3>
              <p>
                Interact with your knowledge base through natural language. Ask questions and get intelligent responses.
              </p>
            </div>

            <div className="feature-card">
              <div className="feature-icon">
                🕸️
              </div>
              <h3>Knowledge Graphs</h3>
              <p>
                Visualize complex relationships between concepts with dynamic, interactive knowledge graphs.
              </p>
            </div>

            <div className="feature-card">
              <div className="feature-icon">
                📄
              </div>
              <h3>Document Processing</h3>
              <p>
                Upload and process various document types to automatically generate knowledge graphs.
              </p>
            </div>

            <div className="feature-card">
              <div className="feature-icon">
                🔍
              </div>
              <h3>Scholarly Search</h3>
              <p>
                Search through academic papers and scholarly sources to expand your knowledge base.
              </p>
            </div>

            <div className="feature-card">
              <div className="feature-icon">
                🔒
              </div>
              <h3>AI Safety</h3>
              <p>
                Built-in content validation and safety measures to ensure reliable information.
              </p>
            </div>

            <div className="feature-card">
              <div className="feature-icon">
                ⚡
              </div>
              <h3>Real-time Updates</h3>
              <p>
                Dynamic updates to your knowledge graphs as new information becomes available.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
