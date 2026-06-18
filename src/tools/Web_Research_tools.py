from langchain.tools import tool

@tool
def Search_Tool(query: str) -> str:
    """
    Search the web for information related to the user's query.

    Args:
        query (str): The search query or topic to look up.

    Returns:
        str: Relevant search results, information, or extracted content
        matching the query.
    """
    return query

@tool
def News_Search(query: str) -> str:
    """
    Search for recent news articles related to the user's query.

    Args:
        query (str): The topic, keyword, or news subject to search for.

    Returns:
        str: Relevant news information or search results related to the query.
    """
    return query