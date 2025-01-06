import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import  RunnableBranch
from langchain_openai import ChatOpenAI


# Load environment variables from .env
load_dotenv()


API_KEY = os.getenv("API_KEY")

model = ChatOpenAI(api_key=API_KEY, model="gpt-3.5-turbo")

classification_prompt_template = ChatPromptTemplate([
    ("system", "You are an expert product reviewer."),
    ("human","Classify the sentiment of this feedback as positive, negative, neutral, or escalate: {feedback}.")
])


# Define prompt templates for different feedback types
positive_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human",
         "Generate a thank you note for this positive feedback: {feedback}."),
    ]
)

negative_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human",
         "Generate a response addressing this negative feedback: {feedback}."),
    ]
)

neutral_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        (
            "human",
            "Generate a request for more details for this neutral feedback: {feedback}.",
        ),
    ]
)

escalate_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        (
            "human",
            "Generate a message to escalate this feedback to a human agent: {feedback}.",
        ),
    ]
)

branches = RunnableBranch(
    (
        lambda input : "positive" in input,
        positive_feedback_template | model | StrOutputParser(),
    ),
    (
        lambda input : "negative" in input,
        negative_feedback_template | model | StrOutputParser(),
    ),
    (
        lambda input : "neutral" in input,
        neutral_feedback_template | model | StrOutputParser(),
    ),
    escalate_feedback_template | model | StrOutputParser(),
)

'''
    A classification chain in LangChain is a process or pipeline that automates the classification of input data (like text) into 
    predefined categories using a combination of prompts, AI models, and output processing. It ensures structured, consistent 
    categorization of data based on instructions provided in the prompt.
'''
classification_chain  = classification_prompt_template | model | StrOutputParser()

prompt = classification_chain |branches

# Run the chain with an example review
# Good review - "The product is excellent. I really enjoyed using it and found it very helpful."
# Bad review - "The product is terrible. It broke after just one use and the quality is very poor."
# Neutral review - "The product is okay. It works as expected but nothing exceptional."
# Default - "I'm not sure about the product yet. Can you tell me more about its features and benefits?"

review = "The product is excellent. I really enjoyed using it and found it very helpful."
result = prompt.invoke({"feedback": review})

print(result)