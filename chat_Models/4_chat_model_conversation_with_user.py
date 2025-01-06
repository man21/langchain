

import os
from traceback import print_tb
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

model =  ChatOpenAI(api_key=API_KEY, model="gpt-3.5-turbo")


chat_history = []

system_message = SystemMessage(content="You are a helpful assistant")
chat_history.append(system_message)


while True:
    query = input("You: ")

    if query.lower() == "exit":
        break

    chat_history.append(HumanMessage(content=query))

    result = model.invoke(chat_history)
    response =  result.content
    chat_history.append(response)

    print(f'AI: {response}')


print("Chat History: ")
print(chat_history)
