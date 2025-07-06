import React, { useState } from 'react';
import OpenAI from 'openai';

const Chat = () => {
  const [messages, setMessages] = useState([
    {
      id: 1,
      type: 'bot',
      content: 'Hello! I\'m DeepBot, your AI knowledge assistant powered by OpenRouter. How can I help you today?',
      timestamp: new Date().toLocaleTimeString()
    }
  ]);
  const [inputMessage, setInputMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  // Initialize OpenRouter client
  const apiKey = import.meta.env.VITE_OPENROUTER_API_KEY;
  console.log('API Key loaded:', apiKey ? 'Yes' : 'No');
  
  const openai = new OpenAI({
    baseURL: "https://openrouter.ai/api/v1",
    apiKey: apiKey,
    dangerouslyAllowBrowser: true,
    defaultHeaders: {
      'HTTP-Referer': 'http://localhost:5173',
      'X-Title': 'DeepBot',
    }
  });

  const handleSendMessage = async (e) => {
    e.preventDefault();
    if (!inputMessage.trim()) return;

    // Add user message
    const userMessage = {
      id: messages.length + 1,
      type: 'user',
      content: inputMessage,
      timestamp: new Date().toLocaleTimeString()
    };
    const updatedMessages = [...messages, userMessage];
    setMessages(updatedMessages);
    setInputMessage('');

    // Call OpenRouter API
    setIsLoading(true);
    try {
      // Check if API key is available
      if (!apiKey) {
        throw new Error('API key not found. Please check your .env file.');
      }

      console.log('Making request to OpenRouter...');
      const completion = await openai.chat.completions.create({
        model: "deepseek/deepseek-chat-v3-0324:free",
        messages: [
          {
            role: "system",
            content: "You are DeepBot, an AI knowledge assistant. You help users with information retrieval, document analysis, and knowledge discovery. Be helpful, concise, and informative."
          },
          ...updatedMessages.map(msg => ({
            role: msg.type === 'user' ? 'user' : 'assistant',
            content: msg.content
          }))
        ],
        max_tokens: 1000,
        temperature: 0.7
      });

      console.log('Response received:', completion);
      const botResponse = completion.choices[0].message.content;

      // Add bot response
      const botMessage = {
        id: messages.length + 2,
        type: 'bot',
        content: botResponse,
        timestamp: new Date().toLocaleTimeString()
      };
      setMessages([...updatedMessages, botMessage]);
    } catch (error) {
      console.error('Detailed error:', error);
      
      let errorMsg = 'Sorry, I encountered an error. ';
      if (error.message.includes('API key')) {
        errorMsg += 'Please check your API key configuration.';
      } else if (error.message.includes('401')) {
        errorMsg += 'Invalid API key. Please check your OpenRouter API key.';
      } else if (error.message.includes('403')) {
        errorMsg += 'Access denied. Please check your OpenRouter account and billing.';
      } else if (error.message.includes('429')) {
        errorMsg += 'Rate limit exceeded. Please try again later.';
      } else {
        errorMsg += `Error: ${error.message}`;
      }
      
      // Add error message
      const errorMessage = {
        id: messages.length + 2,
        type: 'bot',
        content: errorMsg,
        timestamp: new Date().toLocaleTimeString()
      };
      setMessages([...updatedMessages, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-wrapper">
        {/* Chat Header */}
        <div className="chat-header">
          <h2>Chat with DeepBot</h2>
          <p>Ask questions and get AI-powered responses</p>
        </div>

        {/* Messages Container */}
        <div className="messages-container">
          {messages.map((message) => (
            <div
              key={message.id}
              className={`message ${message.type === 'user' ? 'message-user' : 'message-bot'}`}
            >
              <div className="message-content">
                <p>{message.content}</p>
                <span className="message-time">{message.timestamp}</span>
              </div>
            </div>
          ))}
          
          {isLoading && (
            <div className="message message-bot">
              <div className="message-content">
                <div className="typing-indicator">
                  <div className="typing-dot"></div>
                  <div className="typing-dot"></div>
                  <div className="typing-dot"></div>
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Input Form */}
        <div className="chat-input">
          <form onSubmit={handleSendMessage} className="input-form">
            <input
              type="text"
              value={inputMessage}
              onChange={(e) => setInputMessage(e.target.value)}
              placeholder="Ask a question..."
              className="message-input"
              disabled={isLoading}
            />
            <button
              type="submit"
              disabled={isLoading || !inputMessage.trim()}
              className="send-button"
            >
              Send
            </button>
          </form>
        </div>
      </div>

      {/* Quick Actions */}
      <div className="quick-actions">
        <button className="action-card">
          <h3>📚 Upload Documents</h3>
          <p>Add new documents to your knowledge base</p>
        </button>
        <button className="action-card">
          <h3>🔍 Search Scholarly</h3>
          <p>Find academic papers and research</p>
        </button>
        <button className="action-card">
          <h3>🕸️ View Graph</h3>
          <p>Explore knowledge relationships</p>
        </button>
      </div>
    </div>
  );
};

export default Chat;
