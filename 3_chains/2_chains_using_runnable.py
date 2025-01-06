import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableSequence
from langchain_openai import ChatOpenAI


# Load environment variables from .env
load_dotenv()


API_KEY = os.getenv("API_KEY")

model = ChatOpenAI(api_key=API_KEY, model="gpt-3.5-turbo")

prompt = ChatPromptTemplate([
    ("system", "You are a comedian who tells jokes about {topic}."),
    ("human", "Tell me {joke_count} jokes."),
])


format_prompt =  RunnableLambda(lambda inputs: prompt.format(**inputs))
invoke_model = RunnableLambda(lambda inputs: model.invoke(inputs))
parse_output = RunnableLambda(lambda inputs: inputs.content)


chain =  RunnableSequence(first= format_prompt, middle= [invoke_model], last=parse_output)
result = chain.invoke({"topic": "music", "joke_count": 1})

print(result)

