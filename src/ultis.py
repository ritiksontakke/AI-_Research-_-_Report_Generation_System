from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langsmith import Client
import os


load_dotenv()
client = Client()

def get_groq_model():
    return ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY"),
        max_tokens=500,
        temperature=0
    )

def get_system_prompt(prompt_name: str, tag: str ="production") -> str:
    # prompt_name, tag = prompt_name.split(":")

    prompt = client.pull_prompt(f"{prompt_name}:{tag}")
    return prompt.messages[0].prompt.template

def get_gemini_api():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature = 0
    )
def get_openai_model():
    return ChatOpenAI(
        model="gpt-5.4-nano",
        api_key=os.getenv("OPENAI_API_KEY"),
        max_tokens=500,
        temperature=0
    )

def get_model():
    # return get_openai_model()
    pass