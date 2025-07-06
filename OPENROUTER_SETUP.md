# OpenRouter API Setup Instructions

## Step 1: Get Your OpenRouter API Key

1. Visit https://openrouter.ai/
2. Create an account or log in
3. Go to your API Keys section
4. Create a new API key
5. Copy the API key (starts with `sk-or-v1-...`)

## Step 2: Configure Your Environment

1. Open the `.env` file in your project root
2. Replace `your_openrouter_api_key_here` with your actual API key:
   ```
   VITE_OPENROUTER_API_KEY=sk-or-v1-your-actual-key-here
   ```

## Step 3: Start the Development Server

Run the following command in your terminal:
```bash
npm run dev
```

## Step 4: Test the Chat Bot

1. Open your browser and go to `http://localhost:5173`
2. Click on "Get Started" or "Launch DeepBot Chat"
3. Start chatting with the AI bot!

## Available Models

The current setup uses the free model `meta-llama/llama-3.1-8b-instruct:free`, but you can change it to other models available on OpenRouter:

- `anthropic/claude-3.5-sonnet` (paid)
- `openai/gpt-4o` (paid)
- `google/gemini-pro` (paid)
- `meta-llama/llama-3.1-70b-instruct` (paid)

To change the model, edit the `model` parameter in `/src/pages/Chat.jsx`.

## Features

- Real-time chat with AI
- Modern, responsive UI
- Typing indicators
- Message history
- Error handling
- Multiple AI model support via OpenRouter

## Troubleshooting

If you encounter issues:

1. Make sure your API key is correct and properly set in the `.env` file
2. Check that you have credits/balance in your OpenRouter account
3. Verify that your browser developer console doesn't show any errors
4. Try refreshing the page or restarting the development server

## Next Steps

Once the chat is working, you can:
- Integrate with your knowledge graph backend
- Add document upload functionality
- Implement scholarly search features
- Connect to your Neo4j database
- Add user authentication
