import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableParallel
from langchain_openai import ChatOpenAI


# Load environment variables from .env
load_dotenv()


API_KEY = os.getenv("API_KEY")

model = ChatOpenAI(api_key=API_KEY, model="gpt-3.5-turbo")

prompt = ChatPromptTemplate([
    ("system", "You are an expert product reviewer."),
    ("human", "List the main features of the product {product_name}."),
])

# Define pros analysis step
def analyze_pros(features):
    pros_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert product reviewer."),
            (
                "human",
                "Given these features: {features}, list the pros of these features.",
            ),
        ]
    )
    return pros_template.format_prompt(features=features)

# Define cons analysis step
def analyze_cons(features):
    cons_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert product reviewer."),
            (
                "human",
                "Given these features: {features}, list the cons of these features.",
            ),
        ]
    )
    return cons_template.format_prompt(features=features)

pros_branch_chain = (
    RunnableLambda(lambda inputs: analyze_pros(inputs))| model | StrOutputParser()
)


cons_branch_chain = (
    RunnableLambda(lambda inputs: analyze_cons(inputs)) |model | StrOutputParser()
)

def combine_pros_cons(pros, cons):
    return f"Pros: {pros}\n\n\nCons: {cons}"


chain = (
        prompt
        | model
        | StrOutputParser()
        | RunnableParallel(branches={
            "pros": pros_branch_chain, 
            "cons": cons_branch_chain
            })
        | RunnableLambda(lambda inputs: combine_pros_cons(inputs["branches"]["pros"], inputs["branches"]["cons"]))        
)

# Invoke the chain 
result = chain.invoke({"product_name": "Mackbook Pro"})

print(result)