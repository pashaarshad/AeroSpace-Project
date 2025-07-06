import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div className="home-container">
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
              Get Started
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
                🤖
              </div>
              <h3>AI Chat Interface</h3>
              <p>
                Interact with advanced AI models through OpenRouter. Ask questions and get intelligent responses powered by cutting-edge language models.
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
          </div>
        </div>
      </div>

      {/* Getting Started Section */}
      <div className="getting-started">
        <div className="container">
          <h2>Ready to Get Started?</h2>
          <p className="getting-started-subtitle">
            Click the button below to start chatting with DeepBot and experience AI-powered knowledge discovery.
          </p>
          <div className="btn-group">
            <Link to="/chat" className="btn-primary btn-large">
              Launch DeepBot Chat
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
