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
class ResponseOutputParser(BaseOutputParser):
    def parse(self, text: str):
        "Parse the output of an LLM Response."
        # Split the response at 'answer =' and return the parts
        return text.strip().split("answer =")


# Initialize Langchain with OpenAI
openai_llm = ChatOpenAI(api_key=openai_api_key)

# Template for math tutoring
template = """
You are a helpful math tutor that solves math problems and presents the solution with every step.
The output format for each answer should be: answer = <answer here>.
"""

human_template = "{problem}"

# Create a prompt from the template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", template),
        ("human", human_template),
    ]
)

# Example math problem
messages = prompt.format_messages(problem="2x^2−5x+3=0")

# Invoke the LLM with the prompt
response = openai_llm.invoke(messages)

# Parse the response
parsed_response = ResponseOutputParser().parse(response.content)
answer = parsed_response

# Output the steps and the answer
print(answer)
