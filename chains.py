import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from prompts import compliance_prompt

# Load environment variables from .env
load_dotenv()

# Retrieve API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the LLM
llm = ChatOpenAI(model="gpt-4", temperature=0, openai_api_key=api_key)
compliance_chain = LLMChain(
    llm=llm,
    prompt=compliance_prompt
)

compliance_chain = LLMChain(
    llm=llm,
    prompt=compliance_prompt
)
