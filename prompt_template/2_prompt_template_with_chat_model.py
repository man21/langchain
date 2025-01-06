import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain.prompts import ChatPromptTemplate, PromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

load_dotenv()


API_KEY =  os.getenv("API_KEY")

model =  ChatOpenAI(api_key=API_KEY, model="gpt-3.5-turbo")

# Part 1 Basic Prompt template Example
# '''
#  - Simple use cases	
#  - Simple prompts	
#  - More convenient for basic cases
# '''
# basic_template = PromptTemplate.from_template("Hello {name}, How are you?")
# result1 = basic_template.invoke({"name": "Gpt"})
# res = model.invoke(result1)
# print(res.content)



# # Part 2 Basic Prompt Template

# '''
#  - Requires manual setup
#  - More flexible for advanced scenarios
#  - Complex templates or explicit needs
# '''
# # Instantiation using from_template (recommended)
# prompt_advance = PromptTemplate.from_template("Say {foo}")
# result_advance_prompt = prompt_advance.format(foo="bar")

# # Instantiation using initializer
# prompt_advance1 = PromptTemplate(template="Say {foo}")
# result_promptAdvance = model.invoke(prompt_advance1)
# print(result_promptAdvance)






# Part 3 Chat Prompt Template
# chat_prompt_template = ChatPromptTemplate([
#     ("system", "You are a helpful assistant, "),
#     ("user", "Tell me a {adjective} story about a {animal}.")
# ])

# chatPromptResult = chat_prompt_template.invoke({"adjective": "funny", "animal": "cat"})
# result_chatPrompt = model.invoke(chatPromptResult)
# print(result_chatPrompt)


# Part 4  Multiple Message Placeholder with Tuple

# tupleTemplate =  ChatPromptTemplate([
#     ("system","You are a helpful Assistant"),
#     ("user" , "{input}" )
# ])

# tuplePrompt = tupleTemplate.invoke({"input": "How are you"})
# result_tuplePrompt = model.invoke(tuplePrompt)
# print(result_tuplePrompt)

# -------------------------------------------------------------------------------------
# Extra Informoation about Part 4.
# This does work:
# messages = [
#     ("system", "You are a comedian who tells jokes about {topic}."),
#     HumanMessage(content="Tell me 3 jokes."),
# ]
# prompt_template = ChatPromptTemplate.from_messages(messages)
# prompt = prompt_template.invoke({"topic": "lawyers"})
# print("\n----- Prompt with System and Human Messages (Tuple) -----\n")
# print(prompt)

# -----------------------------------------------------------------------------------------------------
# This does NOT work:
# messages = [
#     ("system", "You are a comedian who tells jokes about {topic}."),
#     HumanMessage(content="Tell me {joke_count} jokes."),
# ]
# prompt_template = ChatPromptTemplate.from_messages(messages)
# prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})
# print("\n----- Prompt with System and Human Messages (Tuple) -----\n")
# print(prompt)


# -----------------------------------------------------------------------------------------------------

# Part 5 Building a prompt with chat history:

# messagePlaceHolderPrompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You are a helpful assistant."),
#         MessagesPlaceholder("history"),
#         ("human", "{question}")
#     ]
# )
# messagePlaceHolderResult= messagePlaceHolderPrompt.invoke(
#    {
#        "history": [("human", "what's 5 + 2"), ("ai", "5 + 2 is 7")],
#        "question": "now multiply that by 4"
#    }
# )
# print("Message Placeholder Prompt")
# print(messagePlaceHolderResult)

# Result
# -> ChatPromptValue(messages=[
#     SystemMessage(content="You are a helpful assistant."),
#     HumanMessage(content="what's 5 + 2"),
#     AIMessage(content="5 + 2 is 7"),
#     HumanMessage(content="now multiply that by 4"),
# ])









