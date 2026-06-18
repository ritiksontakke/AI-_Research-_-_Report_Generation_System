from langchain.tools import tool


@tool("Blog_Writer")
def blogwriter(query: str) -> str:
    """
    Generate a complete blog article.

    Use ONLY when the user explicitly asks for:
    - a blog post
    - an article
    - long-form written content

    After generating the blog, return the result and stop.
    Do not call other writing tools after using this tool.
    """
    return f"""
# {query}

## Introduction
This is a sample blog article about {query}.

## Main Content
Artificial Intelligence is transforming industries and changing the way people work and interact with technology.

## Conclusion
AI will continue to shape the future through innovation and automation.
"""


@tool("Summarizer")
def summarizer(query: str) -> str:
    """
    Summarize existing content.

    Use ONLY when the user explicitly requests:
    - a summary
    - key points
    - a short version of text

    Return the summary and stop.
    Do not call Blog_Writer after using this tool.
    """
    text = query[:300]

    return f"""
Summary:
{text}

Key Point:
The content has been condensed into a shorter form highlighting the main ideas.
"""

print(blogwriter.name)