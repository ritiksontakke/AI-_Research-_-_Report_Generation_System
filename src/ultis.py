from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents.middleware import ModelFallbackMiddleware
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langsmith import Client
import os
from langfuse import Langfuse
from langchain.agents.middleware import ModelFallbackMiddleware
from langfuse import Langfuse
# from langfuse import observe

load_dotenv()
langfuse = Langfuse()

client = Client()

def get_groq_model():
    return ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY"),
        max_tokens=500,
        temperature=0,
    )

# def get_system_prompt(prompt_name: str, tag: str ="production") -> str:
#     # prompt_name, tag = prompt_name.split(":")

#     prompt = client.pull_prompt(f"{prompt_name}:{tag}")
#     return prompt.messages[0].prompt.template

def get_gemini_api():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature = 0
    )
def get_openai_model():
    return ChatOpenAI(
        model="gpt-5.4-nano",
        thinking={"type": "enabled", "budget_tokens": 5000},
        api_key=os.getenv("OPENAI_API_KEY"),
        max_tokens=500,
        temperature=0,
    )

def get_model():
    return get_gemini_api(),


fallback = ModelFallbackMiddleware(
    "google_genai:gemini-2.5-flash",
    "openai:gpt-5.4-nano",
)


def get_system_prompt(prompt_name: str = "Ritik Sontakke"):
    try:
        prompt = langfuse.get_prompt(
            prompt_name,
            label="production"  # or "latest"
        )

        # Depending on Langfuse version
        return prompt.prompt

    except Exception as e:
        print(f"Failed to load prompt: {e}")

        return """
        You are an Orchestrator Agent.
        Route tasks to the correct sub-agent.
        Never hallucinate.
        """