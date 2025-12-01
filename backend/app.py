"""
FastAPI backend for AI Tenant Rights Chatbot
This server handles chat requests and uses Langchain + Gemini to answer tenant rights questions
"""

from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Import our AI agent - using direct Google API to avoid model name issues
from utils.direct_gemini import ask_tenant_question_direct as ask_tenant_question

# Load environment variables from .env file
load_dotenv()

app = FastAPI(title="Tenant Rights Chatbot API")

# Enable CORS so our React frontend can talk to this backend
# Using wildcard for simplicity - in production you can restrict to specific domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (simplest for deployment)
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str


@app.get("/")
async def root():
    """Health check endpoint"""
    return {"status": "ok", "message": "Tenant Rights Chatbot API is running"}


@app.options("/chat")
async def chat_options():
    """Handle CORS preflight for chat endpoint"""
    return Response(
        status_code=200,
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST, OPTIONS",
            "Access-Control-Allow-Headers": "*",
        }
    )


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Main chat endpoint - receives a question and returns an AI response
    
    Uses Google Gemini API directly to answer tenant rights questions
    """
    try:
        print(f"Received question: {request.message}")  # Debug log
        
        # Use our AI agent to answer the question
        response_text = ask_tenant_question(request.message)
        
        print(f"Generated response: {response_text[:100]}...")  # Debug log
        
        return ChatResponse(response=response_text)
    
    except ValueError as ve:
        # Specific error for missing API key
        print(f"ValueError: {ve}")  # Debug log
        raise HTTPException(
            status_code=500, 
            detail=f"Configuration error: {str(ve)}"
        )
    except Exception as e:
        # General error handling
        print(f"Exception: {type(e).__name__}: {str(e)}")  # Debug log
        import traceback
        traceback.print_exc()  # Print full error trace
        raise HTTPException(
            status_code=500, 
            detail=f"Error processing request: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

