"""
Langchain setup for the AI tenant rights agent
This module configures the Gemini AI model and creates a specialized agent for answering tenant rights questions
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
import os


def get_llm():
    """
    Initialize and return the Gemini language model
    
    Returns:
        ChatGoogleGenerativeAI: Configured Gemini model instance
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY not found in environment variables. "
            "Make sure you've created a .env file with your API key."
        )
    
    # Initialize Gemini with specific settings
    llm = ChatGoogleGenerativeAI(
        model="models/gemini-1.5-pro",  # Full model path with models/ prefix
        google_api_key=api_key,
        temperature=0.3,  # Lower = more focused and consistent (0-1 scale)
        max_tokens=1000,  # Maximum length of response
    )
    
    return llm


def create_tenant_rights_chain():
    """
    Create a Langchain chain specifically for answering California tenant rights questions
    
    A "chain" in Langchain connects:
    1. A prompt template (instructions for the AI)
    2. The language model (Gemini)
    3. An output parser (formats the response)
    
    Returns:
        A Langchain chain ready to answer tenant questions
    """
    
    # Get the language model
    llm = get_llm()
    
    # Create a prompt template - this is the "system prompt" that tells the AI how to behave
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a knowledgeable and empathetic assistant specializing in California tenant rights and housing law. 

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

Always prioritize the tenant's understanding and wellbeing."""),
        ("human", "{question}")  # This will be replaced with the user's actual question
    ])
    
    # Create the chain: prompt → LLM → output parser
    # The | operator "chains" these components together
    chain = (
        {"question": RunnablePassthrough()}  # Pass the question through
        | prompt                              # Format it with the prompt template
        | llm                                 # Send to Gemini
        | StrOutputParser()                   # Parse the output as a string
    )
    
    return chain


def ask_tenant_question(question: str) -> str:
    """
    Simple function to ask a tenant rights question and get an answer
    
    Args:
        question: The user's question about tenant rights
        
    Returns:
        The AI's response as a string
    """
    chain = create_tenant_rights_chain()
    response = chain.invoke(question)
    return response

