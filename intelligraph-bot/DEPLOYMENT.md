# IntelliGraph Bot - Deployment Guide

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ and npm
- Python 3.9+ and pip
- Neo4j Database (free tier available)
- Git

### 1. Clone the Repository
```bash
git clone <repository-url>
cd intelligraph-bot
```

### 2. Backend Setup
```bash
# Navigate to backend directory
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Copy environment variables
cp .env.example .env

# Edit .env with your API keys and database URLs
nano .env
```

### 3. Frontend Setup
```bash
# Navigate to frontend directory
cd ../frontend

# Install dependencies
npm install

# Install additional packages if needed
npm install react-router-dom d3 lucide-react
```

### 4. Database Setup

#### Neo4j Setup
1. Sign up for Neo4j AuraDB free tier: https://neo4j.com/cloud/aura/
2. Create a new database instance
3. Note down the connection URI, username, and password
4. Update your `.env` file with these credentials

#### Initialize Sample Data
```bash
# Run the knowledge graph initialization
cd backend
python knowledge_graph.py
```

### 5. API Keys Setup

You'll need to sign up for these free services:

#### OpenRouter API
1. Visit: https://openrouter.ai/
2. Sign up for free account
3. Get your API key
4. Add to `.env`: `OPENROUTER_API_KEY=your_key_here`

#### DeepSafe API (Optional)
1. Visit: https://deepsafe.ai/
2. Sign up for free account
3. Get your API key
4. Add to `.env`: `DEEPSAFE_API_KEY=your_key_here`

### 6. Run the Application

#### Start Backend
```bash
cd backend
python app.py
# Server will start on http://localhost:5000
```

#### Start Frontend (in another terminal)
```bash
cd frontend
npm run dev
# App will start on http://localhost:5173
```

### 7. Test the Application

Open your browser and navigate to:
- Frontend: http://localhost:5173
- Backend API: http://localhost:5000/health

## 🌐 Production Deployment

### Option 1: Render.com (Recommended)

#### Backend Deployment
1. Push your code to GitHub
2. Go to Render.com and connect your GitHub repo
3. Create a new Web Service
4. Select your repository
5. Configure build settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Environment**: Python 3.9
6. Add environment variables in Render dashboard
7. Deploy

#### Frontend Deployment
1. Create a new Static Site on Render
2. Select your repository
3. Configure build settings:
   - **Build Command**: `npm run build`
   - **Publish Directory**: `dist`
4. Deploy

### Option 2: Docker Deployment

#### Backend Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

#### Frontend Dockerfile
```dockerfile
FROM node:18-alpine as builder

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

#### Docker Compose
```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "5000:5000"
    environment:
      - OPENROUTER_API_KEY=${OPENROUTER_API_KEY}
      - NEO4J_URI=${NEO4J_URI}
      - NEO4J_USER=${NEO4J_USER}
      - NEO4J_PASSWORD=${NEO4J_PASSWORD}
    depends_on:
      - neo4j

  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend

  neo4j:
    image: neo4j:5.15
    ports:
      - "7474:7474"
      - "7687:7687"
    environment:
      - NEO4J_AUTH=neo4j/password
    volumes:
      - neo4j_data:/data

volumes:
  neo4j_data:
```

## 🔧 Configuration

### Environment Variables

#### Backend (.env)
```env
# API Keys
OPENROUTER_API_KEY=your_openrouter_key
DEEPSAFE_API_KEY=your_deepsafe_key

# Database
NEO4J_URI=neo4j+s://your-instance.databases.neo4j.io
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password

# Flask
FLASK_ENV=production
SECRET_KEY=your_secret_key

# CORS
CORS_ORIGINS=https://your-frontend-domain.com
```

#### Frontend (vite.config.js)
```javascript
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: true
      }
    }
  },
  build: {
    outDir: 'dist',
    assetsDir: 'assets'
  }
})
```

## 📊 Performance Optimization

### Backend Optimizations
1. **Caching**: Implement Redis for frequent queries
2. **Database Indexing**: Add indexes to Neo4j for faster queries
3. **Connection Pooling**: Use connection pooling for database connections
4. **API Rate Limiting**: Implement rate limiting to prevent abuse

### Frontend Optimizations
1. **Code Splitting**: Use React.lazy for component lazy loading
2. **Caching**: Implement service worker for offline capabilities
3. **Compression**: Enable gzip compression
4. **CDN**: Use CDN for static assets

## 🔒 Security Considerations

### Backend Security
1. **API Keys**: Never expose API keys in client-side code
2. **Input Validation**: Validate all user inputs
3. **CORS**: Configure CORS properly for production
4. **Rate Limiting**: Implement rate limiting on all endpoints
5. **HTTPS**: Always use HTTPS in production

### Frontend Security
1. **XSS Protection**: Sanitize user inputs
2. **CSRF Protection**: Implement CSRF tokens
3. **Content Security Policy**: Set appropriate CSP headers
4. **Secure Headers**: Implement security headers

## 🐛 Troubleshooting

### Common Issues

#### Backend Issues
1. **Neo4j Connection Failed**
   - Check your credentials in `.env`
   - Ensure Neo4j instance is running
   - Verify network connectivity

2. **API Key Errors**
   - Verify API keys are correct
   - Check API rate limits
   - Ensure keys have proper permissions

3. **Import Errors**
   - Install missing dependencies: `pip install -r requirements.txt`
   - Check Python version compatibility

#### Frontend Issues
1. **Build Failures**
   - Clear node_modules: `rm -rf node_modules && npm install`
   - Check Node.js version compatibility

2. **API Connection Issues**
   - Verify backend is running
   - Check CORS configuration
   - Ensure API endpoints are correct

### Performance Issues
1. **Slow Queries**
   - Add database indexes
   - Optimize Cypher queries
   - Implement caching

2. **Memory Usage**
   - Monitor memory usage
   - Implement proper cleanup
   - Use connection pooling

## 📈 Monitoring & Analytics

### Health Checks
- Backend: `/health` endpoint
- Frontend: Service worker status
- Database: Neo4j browser monitoring

### Logging
- Backend: Python logging module
- Frontend: Console logging in development
- Production: Structured logging with timestamps

### Metrics
- API response times
- Database query performance
- User interaction analytics
- Error rates and types

## 🚀 Scaling Considerations

### Horizontal Scaling
1. **Load Balancing**: Use nginx or cloud load balancer
2. **Database Clustering**: Neo4j cluster for high availability
3. **CDN**: Static asset delivery via CDN
4. **Caching**: Redis cluster for distributed caching

### Vertical Scaling
1. **Database**: Increase Neo4j memory allocation
2. **Backend**: Increase server resources
3. **Frontend**: Optimize bundle size and loading

## 📞 Support

For deployment issues:
1. Check this deployment guide
2. Review error logs
3. Verify configuration files
4. Test individual components
5. Check API service status

## 🔄 CI/CD Pipeline

### GitHub Actions Example
```yaml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy to Render
        uses: render-action@v1
        with:
          api-key: ${{ secrets.RENDER_API_KEY }}
          service-id: ${{ secrets.RENDER_SERVICE_ID }}
```

---

**Happy Deploying! 🎉**
