import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
api_key = os.getenv('GROQ_API_KEY')

Agent_LLM = ChatGroq(
    model = 'groq/compound-beta',
    api_key = api_key,
    temperature = 0,
    # provider = 'groq'
)

# messages = [
#     ("system", "You are a helpful translator. Translate the user sentence to French."),
#     ("human", "I love programming."),
# ]
# result = Agent_LLM.invoke(messages)
# print(result.content)