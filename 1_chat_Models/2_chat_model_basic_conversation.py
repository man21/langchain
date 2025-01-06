# Chat Model Documents: https://python.langchain.com/v0.3/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/v0.3/docs/integrations/chat/openai/

import os
from dotenv import load_dotenv

from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# get OpenAI KEy from env
API_KEY = os.getenv("API_KEY")

# Create a ChatOpenAI model
model = ChatOpenAI(api_key=API_KEY, model="gpt-3.5-turbo")

messages = [
    SystemMessage(content ="Solve this Math Problem"),
    HumanMessage(content ="what is 81 divided by 9?")
]

result = model.invoke(messages)

print("full Result:- ")
print(result)


print("Only Result: ")
print(result.content)