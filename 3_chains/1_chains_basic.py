import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI


# Load environment variables from .env
load_dotenv()


API_KEY = os.getenv("API_KEY")

model = ChatOpenAI(api_key=API_KEY, model="gpt-3.5-turbo")

prompt = ChatPromptTemplate([
    ("system", "You are a comedian who tells jokes about {topic}."),
    ("human", "Tell me {joke_count} jokes."),
])

# Invoke the chain 
chain = prompt|model |StrOutputParser()
result = chain.invoke({"topic": "music", "joke_count": 1})

print(result)