"""
Alternative Langchain setup using different model initialization
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
import os


def get_llm_v2():
    """
    Alternative LLM initialization that should work with more API versions
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY not found in environment variables. "
            "Make sure you've created a .env file with your API key."
        )
    
    # Try with minimal configuration
    llm = ChatGoogleGenerativeAI(
        google_api_key=api_key,
        temperature=0.3,
    )
    
    return llm


def create_tenant_rights_chain_v2():
    """
    Alternative chain creation
    """
    llm = get_llm_v2()
    
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
        ("human", "{question}")
    ])
    
    chain = (
        {"question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    return chain


def ask_tenant_question_v2(question: str) -> str:
    """
    Alternative version using simplified model initialization
    """
    chain = create_tenant_rights_chain_v2()
    response = chain.invoke(question)
    return response

