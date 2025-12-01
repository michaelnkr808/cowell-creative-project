"""
Direct Google Generative AI implementation (no Langchain wrapper issues)
"""

import google.generativeai as genai
import os


def setup_gemini():
    """Configure the Gemini API directly"""
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY not found in environment variables. "
            "Make sure you've created a .env file with your API key."
        )
    
    genai.configure(api_key=api_key)
    # Use the stable Gemini 2.5 Flash model
    return genai.GenerativeModel('gemini-2.5-flash')


def ask_tenant_question_direct(question: str) -> str:
    """
    Ask a tenant rights question using Google's Gemini API directly
    This bypasses Langchain to avoid model name issues
    """
    
    # System prompt to guide the AI's behavior
    system_prompt = """You are a knowledgeable and empathetic assistant specializing in California tenant rights and housing law.

Your role:
- Provide accurate, helpful information about California tenant rights
- Explain legal concepts in plain, non-technical language
- Be empathetic and supportive - housing issues can be stressful
- If you're not certain about something, say so
- Encourage users to consult a lawyer for complex legal situations

Key areas of knowledge:
- Eviction procedures and notice requirements
- Security deposit laws and refunds
- Habitability standards and repair responsibilities
- Rent control and rent increase limits
- Discrimination and fair housing rights
- Lease terms and tenant-landlord obligations

Always prioritize the tenant's understanding and wellbeing."""
    
    # Combine system prompt with user question
    full_prompt = f"{system_prompt}\n\nUser question: {question}\n\nYour response:"
    
    # Get the model
    model = setup_gemini()
    
    # Generate response
    response = model.generate_content(full_prompt)
    
    return response.text

