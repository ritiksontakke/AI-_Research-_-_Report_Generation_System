# from fastapi import FastAPI
# from src.routes.agent_routes import router

# app = FastAPI(
#     title="Multi Agent API"
# )

# app.include_router(router)

from langchain.tools import tool
from langchain.agents import create_agent
from src.ultis import get_groq_model, get_system_prompt
# from src.ultis import get_gemini_api, get_system_prompt

from src.agents.Coding_Agent import get_code_agents
from src.agents.Content_agent import get_content_agent
from src.agents.web_agents import get_web_agent

class Orchestrator:

    query : str

    def __init__(self, query: str):
        self.query = query

    def get_OrchestratorAgent(self):
        return create_agent(
            model= get_groq_model(),
            tools=[get_content_agent,get_code_agents,get_web_agent],
            system_prompt=get_system_prompt("testing")
        )
    
    def execute_agent(self):
        orchestrator_agent = self.get_OrchestratorAgent()

        result = orchestrator_agent.invoke(
            {"messages": [{"role": "user", "content": self.query}]}
        )

        content = result["messages"][-1].content

        if isinstance(content, list):
            return " ".join(
                block["text"]
                for block in content
                if block.get("type") == "text"
            )

        return str(content)

if __name__ == "__main__":
        query = "Write a blog on AI"
        # query = "Calculate 2 * 2, then add 4 to it. After that, add the previous result to itself. Then add the new result to the previous result. Keep repeating this process until you are sure the answer is complete. you must execute the tools requried loop is file"
        orchestrator = Orchestrator(query)
        result = orchestrator.execute_agent()
        print(f"\n result : {result} \n")