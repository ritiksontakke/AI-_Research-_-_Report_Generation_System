from langchain.tools import tool
from langchain.agents import create_agent
from src.tools.Content_Agent_Tools import Blog_Writer
from src.tools.Content_Agent_Tools import Summarizer
from src.ultis import get_groq_model,get_system_prompt

@tool
def get_content_agent(query:str)->str:
    """
    You are an AI assistant with access to the following tools:

    1. Blog_Writer
    - Generates blog posts, articles, SEO content, and long-form writing.
    - Use when the user requests content creation on a specific topic.
    - Suitable for blogs, articles, guides, tutorials, and marketing content.

    2. Summarizer
    - Summarizes long text into concise and meaningful content.
    - Use when the user provides text and asks for a summary, key points,
        highlights, or a shorter version of the content.

    Tool Selection Guidelines:
    - Use Blog_Writer when the user wants NEW content to be created.
    - Use Summarizer when the user wants EXISTING content condensed.
    - If the request is ambiguous, determine whether the user wants content
    generation or content summarization before selecting a tool.
    - Pass the user's complete request to the selected tool.
    - Return the tool output directly to the user.

    Examples:
    - "Write a blog on Artificial Intelligence" → Blog_Writer
    - "Create an SEO article about Python" → Blog_Writer
    - "Summarize this document" → Summarizer
    - "Give me the key points from this article" → Summarizer
    """
    content_agent = create_agent(
        model=get_groq_model(),
        tools=[Blog_Writer,Summarizer],
        system_prompt=get_system_prompt("testing")
    )
    result = content_agent.invoke({"messages": [{"role" :"user", "content":query}]})
    return result["messages"][-1].content
