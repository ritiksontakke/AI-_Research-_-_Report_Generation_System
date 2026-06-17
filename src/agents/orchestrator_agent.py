from langchain.tools import tool
from langchain.agents import create_agent
from src.ultis import get_groq_model, get_system_prompt
from src.agents.Coding_Agent import get_code_agents
from src.agents.Content_agent import get_content_agent
from src.agents.web_agents import get_web_agent

def get_OrchestratorAgent():
    return create_agent(
        model= get_groq_model(),
        tools=[get_content_agent,get_code_agents,get_web_agent],
        system_prompt=get_system_prompt("testing:production")
    )