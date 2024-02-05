 

# LangChain: How to build AI-driven Applications Tutorial

## Introduction
This repository is a part of LangChain tutorial. It demonstrates the integration of OpenAI model using the LangChain framework. It includes several examples to illustrate the capabilities of LangChain in creating context-aware applications.

## Prerequisites
Before starting, ensure you have the following:

- Python (3.x recommended) installed on your system.
- OpenAI API key (Follow these [instructions](https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/) to get your OpenAI API key)


## Installation

1. **Clone the Repository**: First, clone this repository to your local machine using your preferred method.

2. **Create a Virtual Environment**:

- Navigate to the project directory in your terminal.
- Create a virtual environment:

```

python3 -m venv venv

```

- Activate the virtual environment:
  - On Windows: `venv\Scripts\activate`
  - On MacOS/Linux: `source venv/bin/activate`


1. **Install Requirements**:

- Ensure your virtual environment is active.
- Install the required packages using:

```

pip install -r requirements.txt

```


4. **Set Up OpenAI API Key**:
- Obtain an OpenAI API key (Follow these [instructions](https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/) to get your OpenAI API key.).
- Create a `.env` file in the root of the project directory.
- Add your API key to the file:

```

OPENAI_API_KEY=your_api_key_here

```

  
## Running the Examples

This repository includes several example scripts showcasing different features of LangChain with OpenAI:



1. **Simple Interaction** (`simple_interaction.py`):

- Demonstrates a basic interaction with OpenAI's API.

- Run the script with:

```

python simple_interaction.py

```


2. **Multiple Prompts** (`multiple_prompts.py`):

- Shows how to send multiple prompts to the AI model.

- Run with:

```

python multiple_prompts.py

```


3. **Prompt Templating** (`prompt_templating.py`):

- Illustrates dynamic data injection in prompts.

- Execute the script using:

```

python prompt_templating.py

```


4. **Output Parser** (`output_parser.py`):

- Shows how to parse and refine LLM responses.

- Execute with:

```

python output_parser.py

```  


5. **Chain Integration** (`chain_integration.py`):

- Demonstrates how to streamline processes using LangChain's syntax.

- Run using:

```

python chain_integration.py

```

  



  
