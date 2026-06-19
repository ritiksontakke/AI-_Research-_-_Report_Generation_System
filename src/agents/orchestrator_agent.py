from langchain.tools import tool
from langchain.agents import create_agent
from src.ultis import  get_system_prompt, get_model
from langchain.agents.middleware import ModelCallLimitMiddleware
from src.agents.Coding_Agent import getcodeagents
from src.agents.Content_agent import getcontentagent
from src.agents.web_agents import getwebagent
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents.middleware import ToolCallLimitMiddleware
from src.ultis import fallback

def get_OrchestratorAgent():
        return create_agent(
            model= get_model(),
            tools=[getcontentagent,getcodeagents,getwebagent],
            system_prompt=get_system_prompt("Ritik Sontakke"),
            checkpointer=InMemorySaver(),
            middleware=[
                ModelCallLimitMiddleware(run_limit=5, exit_behavior="end"),
                ToolCallLimitMiddleware(run_limit=5, exit_behavior="end"),
                fallback,
            ]
        )