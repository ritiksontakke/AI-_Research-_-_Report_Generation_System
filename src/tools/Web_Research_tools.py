from langchain.tools import tool

@tool
def Search_Tool(query: str):
    """
    Perform a comprehensive web search to gather information from multiple
    online sources.

    Use this tool when you need:
    - General information about a topic.
    - Background research and context.
    - Official websites, blogs, reports, documentation, or articles.
    - Information about companies, people, products, technologies, or events.
    - Additional sources to support research findings.

    This tool is typically the first step in the research process before
    scraping specific websites or verifying information.
    """
    return f"Searching the web for: {query}"


@tool
def Website_Scraper(url: str):
    """
    Retrieve and extract the main content from a specific webpage.

    Use this tool when:
    - A relevant URL has already been identified.
    - Detailed information from a webpage is required.
    - You need to analyze, summarize, or extract facts from a source.
    - You want to collect evidence, statistics, quotes, or technical details.

    Focus on extracting meaningful content while ignoring unnecessary
    navigation elements, advertisements, and page clutter.
    """
    return f"Scraping website: {url}"


@tool
def News_Search(query: str):
    """
    Search for recent news articles, current events, and emerging developments.

    Use this tool when:
    - The user requests the latest information.
    - Research requires up-to-date events or recent announcements.
    - Tracking industry trends, company updates, market activity,
      policy changes, or breaking news.
    - Information freshness is critical to the answer.

    Prioritize recent and reputable news sources whenever possible.
    """
    return f"Searching latest news for: {query}"