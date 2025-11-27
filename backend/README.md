# Tenant Rights Chatbot - Backend

Python backend using FastAPI, Langchain, and Google Gemini API.

## Setup

1. **Install Python dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Get your Gemini API key:**
   - Go to https://makersuite.google.com/app/apikey
   - Create an API key
   
3. **Create .env file:**
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and add your actual API key.

4. **Run the server:**
   ```bash
   python app.py
   ```
   Server will run on http://localhost:8000

## API Endpoints

- `GET /` - Health check
- `POST /chat` - Send a message, get AI response
  ```json
  {
    "message": "What are my rights if my unit is unsafe?"
  }
  ```

## Project Structure

- `app.py` - Main FastAPI server
- `utils/langchain_setup.py` - Langchain + Gemini configuration
- `utils/vector_store.py` - Document embeddings and RAG
- `documents/` - California tenant rights documents (PDFs/text files)

