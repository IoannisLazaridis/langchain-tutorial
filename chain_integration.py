import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser

# Load environment variables
load_dotenv()

# Retrieve the OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")


# Custom output parser class
class CommaSeparatedListOutputParser(BaseOutputParser):
    def parse(self, text: str):
        return text.strip().split(", ")


# Initialize Langchain with OpenAI
openai_llm = ChatOpenAI(api_key=openai_api_key)

# Template for generating comma-separated lists
template = """
You are a capable assistant specialized in creating concise comma-separated lists.
Upon receiving a specific category from a user, your task is to promptly generate a list of five relevant items within that category,
formatted exclusively as a comma-separated sequence.
Your response should consist solely of this list, without any additional text or explanation.
"""

# Template for human input
human_template = "{text}"

# Create a prompt from the templates
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", template),
        ("human", human_template),
    ]
)

# Create the chain using the pipe operator
chain = prompt | openai_llm | CommaSeparatedListOutputParser()

# Invoke the chain with the necessary input
response = chain.invoke({"text": "colors"})

print(response)
