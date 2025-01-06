# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/openai/

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# get OpenAI KEy from env
API_KEY = os.getenv("API_KEY")

# Create a ChatOpenAI model
model = ChatOpenAI(api_key=API_KEY, model="gpt-3.5-turbo")

# Invoke the model with a input
result =  model.invoke("What is 81 divided by 9?")

print("Full Result: ")
print(result)

print("Content Only: ")
print(result.content)


