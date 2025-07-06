import React from 'react';
import { Link, useLocation } from 'react-router-dom';

const Header = () => {
  const location = useLocation();
  
  const isActive = (path) => {
    return location.pathname === path ? 'text-blue-600 border-b-2 border-blue-600' : 'text-gray-600 hover:text-blue-600';
  };

  return (
    <header className="bg-white shadow-lg">
      <div className="container">
        <div className="flex justify-between items-center h-16">
          <div className="flex items-center">
            <Link to="/" className="text-2xl font-bold text-gray-900">
              <span className="text-blue-600">Deep</span>Bot
            </Link>
          </div>
          
          <nav className="flex space-x-4">
            <Link to="/" className={`text-lg font-medium ${isActive('/')}`}>Home</Link>
            <Link to="/chat" className={`text-lg font-medium ${isActive('/chat')}`}>Chat</Link>
            <Link to="/graph" className={`text-lg font-medium ${isActive('/graph')}`}>Knowledge Graph</Link>
            <Link to="/about" className={`text-lg font-medium ${isActive('/about')}`}>About</Link>
          </nav>
          
          <div className="flex items-center">
            <button className="btn-primary">Get Started</button>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
