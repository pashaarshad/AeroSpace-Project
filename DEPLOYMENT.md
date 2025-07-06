# Deployment Configuration

## Frontend Deployment (Netlify)

### 1. Build Settings
- **Build Command**: `npm run build`
- **Publish Directory**: `dist`
- **Node Version**: 18+

### 2. Environment Variables (Netlify)
Add these in Netlify dashboard:
```
VITE_OPENROUTER_API_KEY=your_openrouter_api_key
VITE_BACKEND_URL=https://your-backend-url.railway.app
```

### 3. Build Configuration
Create `netlify.toml` in project root:
```toml
[build]
  command = "npm run build"
  publish = "dist"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

## Backend Deployment (Railway/Render)

### 1. Railway Deployment
- Connect GitHub repository
- Select backend folder: `intelligraph-bot/backend`
- Set Python runtime
- Add environment variables

### 2. Environment Variables (Railway)
```
OPENROUTER_API_KEY=your_openrouter_api_key
DEEPSAFE_API_KEY=your_deepsafe_api_key
NEO4J_URI=your_neo4j_uri
NEO4J_USER=your_neo4j_user
NEO4J_PASSWORD=your_neo4j_password
PORT=5000
```

### 3. Procfile for Railway
Create `Procfile` in backend directory:
```
web: python app.py
```

### 4. Requirements.txt
Ensure all dependencies are listed:
```
Flask==2.3.3
flask-cors==4.0.0
python-dotenv==1.0.0
requests==2.31.0
neo4j==5.13.0
```

## Alternative Options

### Frontend Alternatives:
- **Vercel** (excellent for React)
- **GitHub Pages** (free, but static only)
- **Surge.sh** (simple deployment)

### Backend Alternatives:
- **Render** (great Python support)
- **Heroku** (paid plans only now)
- **DigitalOcean App Platform**
- **AWS Elastic Beanstalk**

## Database Options
- **Neo4j AuraDB** (cloud Neo4j)
- **GrapheneDB** (Neo4j hosting)
- **Local development**: Use Neo4j Desktop

## Recommended Stack:
1. **Frontend**: Netlify (free)
2. **Backend**: Railway (free tier)
3. **Database**: Neo4j AuraDB (free tier)
4. **Domain**: Custom domain via Netlify

## Cost Breakdown:
- **Netlify**: Free (100GB bandwidth/month)
- **Railway**: Free ($5/month after trial)
- **Neo4j AuraDB**: Free tier available
- **Total**: ~$5/month for full stack
