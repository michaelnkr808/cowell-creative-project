# AI Tenant Rights Access Tool

An AI-powered chatbot that helps California tenants understand their housing rights in plain, non-technical language. This tool aims to bridge the information gap between complex housing laws and the people who need to understand them.

## 🎯 Project Goals

Many tenants don't know their rights regarding:
- Eviction procedures and notice requirements
- Unsafe living conditions and repair responsibilities  
- Security deposits and refunds
- Discrimination and fair housing
- Rent increases and lease terms

This chatbot uses AI and retrieval-augmented generation (RAG) to answer these questions using official California legal resources.

## 🏗️ Architecture

- **Frontend**: React + TypeScript (Vite)
- **Backend**: Python + FastAPI
- **AI Model**: Google Gemini API via Langchain
- **Vector Database**: FAISS (local, no external services needed)
- **Document Sources**: Official California tenant rights guides

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ and npm
- Python 3.9+
- Google Gemini API key (free tier available)

### 1. Clone and Install

```bash
# Install frontend dependencies
npm install

# Install backend dependencies
cd backend
pip install -r requirements.txt
```

### 2. Set Up API Key

```bash
cd backend
echo "GOOGLE_API_KEY=your_actual_key_here" > .env
```

Get your API key at: https://makersuite.google.com/app/apikey

### 3. Add Legal Documents

Download the California Tenants Guide and place it in `backend/documents/`:
- [2025 California Tenants Guide PDF](https://www.dre.ca.gov/publications/ResourceGuidebook/2025_Landlord_Tenant_Guide.pdf)

### 4. Run the Application

**Terminal 1 - Backend:**
```bash
cd backend
python app.py
# Server runs on http://localhost:8000
```

**Terminal 2 - Frontend:**
```bash
npm run dev
# App runs on http://localhost:5173
```

## 📁 Project Structure

```
cowell-creative-project/
├── src/                    # React frontend
│   ├── App.tsx            # Main chat interface
│   ├── components/        # React components
│   └── ...
├── backend/               # Python backend
│   ├── app.py            # FastAPI server
│   ├── utils/            # Langchain & RAG setup
│   ├── documents/        # Legal documents (PDFs)
│   └── requirements.txt  # Python dependencies
└── README.md             # You are here
```

## 🔧 How It Works

1. **User asks a question** in the React chat interface
2. **Frontend sends** the question to the FastAPI backend
3. **Backend retrieves** relevant sections from legal documents using vector search
4. **Gemini AI** generates a response based on the retrieved context
5. **Frontend displays** the answer in plain language

## 🎓 Learning Resources

This project demonstrates:
- **Full-stack development** (React + Python)
- **API integration** (REST APIs, HTTP requests)
- **AI/ML concepts** (embeddings, vector search, RAG)
- **Real-world application** of technology for social good

## 📝 Development Roadmap

- [x] Project setup and architecture
- [x] Basic frontend chat interface
- [x] FastAPI backend skeleton
- [ ] Langchain + Gemini integration
- [ ] RAG pipeline with FAISS
- [ ] Document processing and indexing
- [ ] Production deployment

## ⚖️ Legal Disclaimer

This tool provides general information about California tenant rights and should not be considered legal advice. For specific legal issues, consult a qualified attorney.

## 📄 License

MIT License - See LICENSE file for details

---

**Built for housing justice education** 🏠
