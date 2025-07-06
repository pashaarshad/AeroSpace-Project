import React, { useState, useEffect } from 'react';
import OpenAI from 'openai';

const DebugChat = () => {
  const [debugInfo, setDebugInfo] = useState({});
  const [testResult, setTestResult] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    const apiKey = import.meta.env.VITE_OPENROUTER_API_KEY;
    setDebugInfo({
      apiKeyExists: !!apiKey,
      apiKeyLength: apiKey ? apiKey.length : 0,
      apiKeyPrefix: apiKey ? apiKey.substring(0, 15) + '...' : 'None'
    });
  }, []);

  const testAPI = async () => {
    setIsLoading(true);
    setTestResult('Testing...');
    
    try {
      const apiKey = import.meta.env.VITE_OPENROUTER_API_KEY;
      
      if (!apiKey) {
        throw new Error('API key not found in environment variables');
      }

      const openai = new OpenAI({
        baseURL: "https://openrouter.ai/api/v1",
        apiKey: apiKey,
        dangerouslyAllowBrowser: true,
        defaultHeaders: {
          'HTTP-Referer': 'http://localhost:5173',
          'X-Title': 'DeepBot',
        }
      });

      const completion = await openai.chat.completions.create({
        model: "microsoft/phi-3-mini-128k-instruct:free",
        messages: [
          {
            role: "user",
            content: "Say 'Hello, test successful!'"
          }
        ],
        max_tokens: 50
      });

      setTestResult('✅ SUCCESS: ' + completion.choices[0].message.content);
    } catch (error) {
      setTestResult('❌ ERROR: ' + error.message);
      console.error('Full error:', error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'monospace' }}>
      <h2>OpenRouter Debug Panel</h2>
      
      <div style={{ marginBottom: '20px' }}>
        <h3>Environment Variables:</h3>
        <p>API Key Exists: {debugInfo.apiKeyExists ? '✅ Yes' : '❌ No'}</p>
        <p>API Key Length: {debugInfo.apiKeyLength}</p>
        <p>API Key Prefix: {debugInfo.apiKeyPrefix}</p>
      </div>

      <div style={{ marginBottom: '20px' }}>
        <h3>API Test:</h3>
        <button 
          onClick={testAPI} 
          disabled={isLoading}
          style={{
            padding: '10px 20px',
            fontSize: '16px',
            backgroundColor: '#007bff',
            color: 'white',
            border: 'none',
            borderRadius: '5px',
            cursor: isLoading ? 'not-allowed' : 'pointer'
          }}
        >
          {isLoading ? 'Testing...' : 'Test API Connection'}
        </button>
      </div>

      <div style={{ marginBottom: '20px' }}>
        <h3>Test Result:</h3>
        <pre style={{ 
          backgroundColor: '#f8f9fa', 
          padding: '10px', 
          borderRadius: '5px',
          whiteSpace: 'pre-wrap',
          wordBreak: 'break-word'
        }}>
          {testResult || 'No test run yet'}
        </pre>
      </div>

      <div>
        <h3>Instructions:</h3>
        <ol>
          <li>Make sure your .env file is in the project root</li>
          <li>Ensure the API key doesn't have quotes around it</li>
          <li>Restart the development server after changing .env</li>
          <li>Check the browser console for additional error details</li>
        </ol>
      </div>
    </div>
  );
};

export default DebugChat;
