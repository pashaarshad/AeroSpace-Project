import React from 'react';

const Footer = () => {
  return (
    <footer className="bg-gray-800 text-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div>
            <h3 className="text-lg font-semibold mb-4">DeepBot</h3>
            <p className="text-gray-400">
              AI-powered knowledge retrieval system with dynamic knowledge graphs.
            </p>
          </div>
          
          <div>
            <h4 className="text-sm font-semibold mb-4 uppercase">Features</h4>
            <ul className="text-gray-400 space-y-2">
              <li>AI Chat Interface</li>
              <li>Knowledge Graphs</li>
              <li>Document Processing</li>
              <li>Scholarly Search</li>
            </ul>
          </div>

          <div>
            <h4 className="text-sm font-semibold mb-4 uppercase">Technology</h4>
            <ul className="text-gray-400 space-y-2">
              <li>React + Vite</li>
              <li>Flask Backend</li>
              <li>Neo4j Database</li>
              <li>OpenRouter AI</li>
            </ul>
          </div>
          
          <div>
            <h4 className="text-sm font-semibold mb-4 uppercase">Connect</h4>
            <ul className="text-gray-400 space-y-2">
              <li>GitHub</li>
              <li>Documentation</li>
              <li>API Reference</li>
              <li>Support</li>
            </ul>
          </div>

          <div>
            <h4 className="text-sm font-semibold mb-4 uppercase">Resources</h4>
            <ul className="text-gray-400 space-y-2">
              <li>Documentation</li>
              <li>API Reference</li>
              <li>Support</li>
            </ul>
          </div>

          <div>
            <h4 className="text-sm font-semibold mb-4 uppercase">Contact</h4>
            <p className="text-gray-400">Email: support@deepbot.ai</p>
            <p className="text-gray-400">Phone: +1 234 567 890</p>
          </div>
        </div>
        
        <div className="border-t border-gray-700 mt-8 pt-8 text-center text-gray-400">
          <p>&copy; 2025 DeepBot. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
