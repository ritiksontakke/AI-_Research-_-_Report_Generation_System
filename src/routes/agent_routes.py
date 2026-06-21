from fastapi import APIRouter
from pydantic import BaseModel
from src.agents.orchestrator_agent import get_OrchestratorAgent
from langfuse.callback import CallbackHandler
from fastapi.responses import StreamingResponse

router = APIRouter()

orchestrator = get_OrchestratorAgent()

class QueryRequest(BaseModel):
    query : str
    thread_id: str

@router.get("/")
def home():
    return{"messages" : "QueryRequest agent is running"}

@router.post("/orchestrator_agent")
async def execute_agent(request: QueryRequest):
    handler = CallbackHandler()

    result = orchestrator.invoke(
        {
            "messages": [
                {
                    "role" : "user",
                    "content" : request.query
                }
            ]
        },
        config={"configurable": {"thread_id": request.thread_id},"callbacks": [handler]},
    )
    return{
        "query": request.query,
        "response" : result["messages"][-1].content
    }

@router.post("/orchestrator-agent-stream")
async def execute_agent_stream(request: QueryRequest):

    async def generate():

        async for chunk, metadata in orchestrator.astream(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": request.query
                    }
                ]
            },
            stream_mode="messages",
            config={
                "configurable": {
                    "thread_id": request.thread_id
                }
            }
        ):
            if hasattr(chunk, "content") and chunk.content:
                yield chunk.content

    return StreamingResponse(
        generate(),
        media_type="text/plain"
    )