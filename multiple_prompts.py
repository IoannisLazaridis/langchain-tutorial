import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

# Load environment variables
load_dotenv()

# Retrieving OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initializing LangChain with OpenAI
openai_llm = ChatOpenAI(api_key=openai_api_key)

# Creating an array of prompts
prompts = [
    HumanMessage(
        content="Imagine you are Darth Vader, and respond in a manner consistent with his character."
    ),
    HumanMessage(
        content="Provide math tutoring while staying in character as Darth Vader."
    ),
    HumanMessage(content="what is 1 + 1?"),
]

# Invoking the prompts
response = openai_llm.invoke(prompts)
print(response.content)
