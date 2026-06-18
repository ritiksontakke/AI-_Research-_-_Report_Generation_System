from langchain.tools import tool


@tool("Search_Tool")
def searchtool(query: str) -> str:
    """
    Search for general information on a topic.

    Use ONLY when the user requests:
    - general information
    - explanations
    - facts
    - background research
    - educational content

    Do NOT use for:
    - breaking news
    - recent events
    - current affairs

    Return the search result and stop.
    Do not call News_Search after using this tool unless the user explicitly asks for recent news.
    """
    return f"Search Result: {query}"


@tool("News_Search")
def newssearch(query: str) -> str:
    """
    Search for recent news and current events.

    Use ONLY when the user requests:
    - latest news
    - recent updates
    - current events
    - today's developments

    Do NOT use for:
    - general knowledge
    - educational explanations
    - historical information

    Return the news result and stop.
    Do not call Search_Tool after using this tool unless additional background information is explicitly required.
    """
    return f"News Result: {query}"