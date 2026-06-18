from fastapi import APIRouter
from pydantic import BaseModel

from src.agents.orchestrator_agent import get_OrchestratorAgent

router = APIRouter()

orchestrator = get_OrchestratorAgent()

class QueryRequest(BaseModel):
    query : str
    thread_id: str

@router.get("/")
def home():
    return{"messages" : "QueryRequest agent is running"}

@router.post("/orchestrator_agent")
def execute_agent(request: QueryRequest):

    result = orchestrator.invoke(
        {
            "messages": [
                {
                    "role" : "user",
                    "content" : request.query
                }
            ]
        },
        config={"configurable": {"thread_id": request.thread_id}},
    )
    return{
        "query": request.query,
        "response" : result["messages"][-1].content
    }

