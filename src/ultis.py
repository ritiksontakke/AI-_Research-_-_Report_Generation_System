from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langsmith import Client
import os



load_dotenv()
client = Client()

def get_groq_model():
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0
    )

def get_system_prompt(prompt_name: str, tag: str ="production") -> str:
    # prompt_name, tag = prompt_name.split(":")

    prompt = client.pull_prompt(f"{prompt_name}:{tag}")
    return prompt.messages[0].prompt.template

def get_gemini_api():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature = 0
    )