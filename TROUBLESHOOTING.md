# OpenRouter Troubleshooting Guide

## Issue: Getting API errors when trying to chat

### Possible Causes:
1. **API Key Issues**: Wrong format, expired, or insufficient credits
2. **Model Issues**: Model name incorrect or unavailable
3. **CORS Issues**: Browser blocking the request
4. **Network Issues**: Connection problems

### Solutions:

#### 1. Check API Key Format
- Make sure `.env` file has: `VITE_OPENROUTER_API_KEY=sk-or-v1-...` (no quotes)
- Restart dev server after changing .env: `npm run dev`

#### 2. Verify OpenRouter Account
- Go to https://openrouter.ai/
- Check your account balance/credits
- Verify API key is active

#### 3. Test Different Models
Try these free models in order:
- `microsoft/phi-3-mini-128k-instruct:free`
- `meta-llama/llama-3.1-8b-instruct:free`
- `google/gemma-2-9b-it:free`

#### 4. Debug Steps
1. Visit `/debug` route in your app
2. Check browser console for detailed errors
3. Verify API key is loading correctly

#### 5. Alternative: Use Fetch API
If OpenAI SDK doesn't work, try direct fetch:

```javascript
const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${apiKey}`,
    'Content-Type': 'application/json',
    'HTTP-Referer': 'http://localhost:5173',
    'X-Title': 'DeepBot'
  },
  body: JSON.stringify({
    model: 'microsoft/phi-3-mini-128k-instruct:free',
    messages: [{ role: 'user', content: 'Hello' }]
  })
});
```

#### 6. Check Network
- Disable browser extensions
- Try incognito mode
- Check if VPN is interfering

### Next Steps:
1. Go to `/debug` route first
2. Test API connection
3. Check browser console for errors
4. Try different model if needed
