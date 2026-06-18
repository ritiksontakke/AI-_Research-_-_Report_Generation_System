from langchain.tools import tool


@tool("Blog_Writer")
def Blog_Writer(query: str) -> str:
    """
    Create a complete blog article from a user-supplied topic or prompt.

    This tool takes a blog topic, question, or content brief and generates
    a coherent, engaging, and informative blog post. The generated article
    may include a title, introduction, section headings, body content, and
    conclusion depending on the provided instructions.

    Args:
        query (str): The blog topic, content requirements, keywords,
            target audience, or any additional writing instructions.

    Returns:
        str: The generated blog post in plain text or markdown format.
    """
    blog = f"# {query}\n\nThis is a sample blog article about {query}."
    return blog


@tool("Summarizer")
def Summarizer(query: str) -> str:
    """
    Summarize the provided text into a concise and clear summary.

    Args:
        query (str): The text, article, document, or content to summarize.

    Returns:
        str: A concise summary highlighting the key points and main ideas
        from the provided content.
    """
    return f"Summarize the following text in a concise manner:\n\n{query}"