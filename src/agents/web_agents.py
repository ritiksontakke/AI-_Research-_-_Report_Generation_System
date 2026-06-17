from langchain.agents import create_agent
from src.ultis import get_groq_model,get_system_prompt
from src.tools.Web_Research_tools import News_Search,Search_Tool,Website_Scraper
from langchain.tools import tool

@tool
def get_web_agent(query:str)->str:
    """
    You are a web research agent responsible for finding accurate,
    comprehensive, and up-to-date information.

    Tool Selection Guidelines:

    - Search_Tool:
      Use for general web searches, background research, discovering
      relevant websites, official documentation, and authoritative sources.

    - Website_Scraper:
      Use after identifying a useful URL. Extract the main content of the
      webpage and gather detailed information, evidence, statistics, and
      technical details.

    - News_Search:
      Use when the user asks for the latest information, current events,
      recent announcements, trends, market updates, or anything where
      freshness matters.

    Workflow:
    1. Determine whether the query requires general research, detailed page
       analysis, recent news, or a combination.
    2. Search for relevant sources using Search_Tool and/or News_Search.
    3. Scrape important sources using Website_Scraper when deeper analysis
       is needed.
    4. Combine findings from multiple sources.
    5. Return a clear, accurate, and well-structured answer.

    Always choose the minimum number of tools required while ensuring
    completeness and accuracy.
    """
    web_agent=create_agent(
        model=get_groq_model(),
        tools=[News_Search,Search_Tool,Website_Scraper],
        system_prompt=get_system_prompt("testing")
    )
    result = web_agent.invoke({"messages": [{"role" : "user", "content" : query}]})
    return result["messages"][-1].content