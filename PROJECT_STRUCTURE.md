# IntelliGraph Bot - Complete Project Structure

## 📁 Project Directory Structure

```
intelligraph-bot/
├── frontend/                   # React.js Frontend
│   ├── src/
│   │   ├── components/
│   │   │   ├── Chat/
│   │   │   │   ├── ChatInterface.jsx
│   │   │   │   ├── MessageBubble.jsx
│   │   │   │   ├── InputBar.jsx
│   │   │   │   └── TypingIndicator.jsx
│   │   │   ├── Graph/
│   │   │   │   ├── KnowledgeGraph.jsx
│   │   │   │   ├── GraphVisualization.jsx
│   │   │   │   └── NodeDetails.jsx
│   │   │   ├── Layout/
│   │   │   │   ├── Header.jsx
│   │   │   │   ├── Sidebar.jsx
│   │   │   │   └── Footer.jsx
│   │   │   └── Common/
│   │   │       ├── Button.jsx
│   │   │       ├── Modal.jsx
│   │   │       └── Loading.jsx
│   │   ├── pages/
│   │   │   ├── Home.jsx
│   │   │   ├── Chat.jsx
│   │   │   ├── Graph.jsx
│   │   │   ├── About.jsx
│   │   │   └── Documentation.jsx
│   │   ├── hooks/
│   │   │   ├── useChat.js
│   │   │   ├── useGraph.js
│   │   │   └── useAuth.js
│   │   ├── services/
│   │   │   ├── api.js
│   │   │   ├── graph.js
│   │   │   └── auth.js
│   │   ├── utils/
│   │   │   ├── constants.js
│   │   │   └── helpers.js
│   │   └── styles/
│   │       ├── globals.css
│   │       └── components.css
│   ├── public/
│   │   ├── index.html
│   │   └── favicon.ico
│   ├── package.json
│   └── tailwind.config.js
│
├── backend/                    # Python Flask Backend
│   ├── app/
│   │   ├── __init__.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── chat.py
│   │   │   ├── graph.py
│   │   │   ├── auth.py
│   │   │   └── upload.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── ai_service.py
│   │   │   ├── graph_service.py
│   │   │   ├── scholar_service.py
│   │   │   └── deepsafe_service.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── chat.py
│   │   │   └── knowledge.py
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   ├── nlp_processor.py
│   │   │   ├── pdf_parser.py
│   │   │   └── graph_builder.py
│   │   └── config/
│   │       ├── __init__.py
│   │       ├── settings.py
│   │       └── database.py
│   ├── data/
│   │   ├── static/
│   │   │   ├── faqs.md
│   │   │   ├── policies.md
│   │   │   └── guides.md
│   │   ├── dynamic/
│   │   │   ├── uploads/
│   │   │   └── cache/
│   │   └── graphs/
│   │       ├── ontology.owl
│   │       └── schema.json
│   ├── tests/
│   │   ├── test_routes.py
│   │   ├── test_services.py
│   │   └── test_utils.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── run.py
│
├── docs/                       # Documentation
│   ├── API.md
│   ├── SETUP.md
│   ├── ARCHITECTURE.md
│   └── DEPLOYMENT.md
│
├── scripts/                    # Utility Scripts
│   ├── setup_neo4j.py
│   ├── data_ingestion.py
│   └── deploy.sh
│
├── .env.example
├── .gitignore
├── README.md
├── docker-compose.yml
└── package.json
```

## 🎯 Page-by-Page Breakdown

### 1. **Home Page** (`/`)
**Purpose**: Welcome and introduction
**Features**:
- Hero section with project description
- "Start Chat" CTA button
- Features overview
- Technology showcase
- Live demo button

### 2. **Chat Interface** (`/chat`)
**Purpose**: Main AI interaction
**Features**:
- Real-time chat interface
- Message history
- Typing indicators
- File upload for documents
- Export conversation
- Sidebar with quick actions

### 3. **Knowledge Graph** (`/graph`)
**Purpose**: Visualize the knowledge network
**Features**:
- Interactive graph visualization
- Node filtering and search
- Entity relationship explorer
- Graph statistics
- Add/edit knowledge nodes

### 4. **Documentation** (`/docs`)
**Purpose**: Project documentation
**Features**:
- API documentation
- How it works
- Technology stack
- Use cases
- Developer guide

### 5. **About** (`/about`)
**Purpose**: Project information
**Features**:
- Team information
- Project goals
- Technology details
- Contact information
- GitHub links

## 🔄 Data Flow Architecture

```
User Query → React UI → Flask API → DeepSafe Validation
                              ↓
                        Intent Classification
                              ↓
                    ┌─────────────────────┐
                    │   Query Router      │
                    └─────────────────────┘
                              ↓
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
   Static KG            Vector Search         Scholar Search
   (Neo4j)              (LlamaIndex)         (APIs)
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              ↓
                    Response Aggregation
                              ↓
                    LLM Processing (OpenRouter)
                              ↓
                    Safety Check (DeepSafe)
                              ↓
                    Formatted Response → React UI
```
