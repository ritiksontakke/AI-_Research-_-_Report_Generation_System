from langchain.tools import tool
from langchain.agents import create_agent
from src.ultis import get_groq_model, get_system_prompt
from langchain.agents.middleware import ModelCallLimitMiddleware
from src.agents.Coding_Agent import getcodeagents
from src.agents.Content_agent import getcontentagent
from src.agents.web_agents import getwebagent

def get_OrchestratorAgent():
        return create_agent(
            model= get_groq_model(),
            tools=[getcontentagent,getcodeagents,getwebagent],
            system_prompt=get_system_prompt("testing"),
            middleware=[
                 ModelCallLimitMiddleware(
                      thread_limit=10,
                      run_limit=5,
                      exit_behavior="end",
                )
            ]
        )