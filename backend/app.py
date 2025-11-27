"""
FastAPI backend for AI Tenant Rights Chatbot
This server handles chat requests and uses Langchain + Gemini to answer tenant rights questions
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = FastAPI(title="Tenant Rights Chatbot API")

# Enable CORS so our React frontend can talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite's default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define what data we expect from the frontend
class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str


@app.get("/")
async def root():
    """Health check endpoint"""
    return {"status": "ok", "message": "Tenant Rights Chatbot API is running"}


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Main chat endpoint - receives a question and returns an AI response
    
    This is where we'll integrate Langchain + Gemini + RAG
    For now, it's a simple echo to test the connection
    """
    try:
        # TODO: Add Langchain + Gemini integration here
        # For now, just echo back
        response_text = f"You asked: {request.message}. (AI integration coming next!)"
        
        return ChatResponse(response=response_text)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    # Run the server on port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)

