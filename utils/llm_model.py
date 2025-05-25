import os
from dotenv import load_dotenv
from langchain_groq import chatgroq

load_dotenv()

Agent_LLM = ChatGroq(
    api_key = os.getenv('GROQ_API_KEY')
    model = 'llama-3.1-70b-instant'
    temperature = 0
)