import OpenAI from 'openai';

// Test the OpenRouter API key
const apiKey = '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';

const openai = new OpenAI({
  baseURL: "https://openrouter.ai/api/v1",
  apiKey: apiKey,
  dangerouslyAllowBrowser: true,
  defaultHeaders: {
    'HTTP-Referer': 'http://localhost:5173',
    'X-Title': 'DeepBot',
  }
});

async function testAPI() {
  try {
    console.log('Testing OpenRouter API...');
    const completion = await openai.chat.completions.create({
      model: "meta-llama/llama-3.1-8b-instruct:free",
      messages: [
        {
          role: "user",
          content: "Hello, can you respond with just 'API test successful'?"
        }
      ],
      max_tokens: 50
    });

    console.log('Success:', completion.choices[0].message.content);
  } catch (error) {
    console.error('API Test Error:', error);
  }
}

// Export for testing
export { testAPI };
