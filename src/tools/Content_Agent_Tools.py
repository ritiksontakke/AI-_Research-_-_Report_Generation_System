from langchain.tools import tool

@tool("Blog_Writer")
def Blog_Writer(query: str):
    """
    Tool Name: Blog_Writer

    Use this tool to generate blog posts, articles, and long-form content
    based on a given topic or set of requirements.

    When to use:
    - User requests a blog post.
    - User wants SEO content.
    - User wants an article on a specific topic.

    Args:
        query (str): Topic, title, or instructions for the blog.

    Returns:
        str: A complete blog post based on the provided requirements.
    """
    return f"Blog Writer Tool Activated.\n\nBlog Request: {query}"

@tool("Summarizer")
def Summarizer(query: str):
    """
    Tool Name: Summarizer

    Use this tool to summarize long text into concise and meaningful content.

    When to use:
    - User requests a summary.
    - User provides lengthy text.
    - User wants key points extracted.

    Args:
        query (str): Text content to summarize.

    Returns:
        str: A concise summary of the provided content.
    """
    return f"Summarizer Tool Activated.\n\nContent To Summarize: {query}"

@tool("Summarizer")
def Summarizer(query: str):
    """
    Tool Name: Summarizer

    Use this tool to summarize long text into concise and meaningful content.

    When to use:
    - User requests a summary.
    - User provides lengthy text.
    - User wants key points extracted.

    Args:
        query (str): Text content to summarize.

    Returns:
        str: A concise summary of the provided content.
    """
    return f"Summarizer Tool Activated.\n\nContent To Summarize: {query}"
