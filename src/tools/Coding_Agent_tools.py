from langchain.tools import tool

@tool("Code_Generator")
def Code_Generator(query: str)-> str:
    """
    Tool Name: Code_Generator

    Use this tool to generate source code based on user requirements.

    When to use:
    - User requests code implementation.
    - User wants a function, class, script, or application.
    - User asks for code in a specific programming language.
    - User wants example code for a concept or feature.

    Args:
        query (str): Description of the code requirements.

    Returns:
        str: Generated source code based on the provided requirements.
    """
    return f"Code Generator Tool Activated.\n\nCode Generation Request: {query}"


@tool("Code_Reviewer")
def Code_Reviewer(query: str):
    """
    Tool Name: Code_Reviewer

    Use this tool to review source code and provide feedback on
    code quality, best practices, performance, readability, and
    potential issues.

    When to use:
    - User requests a code review.
    - User wants feedback on existing code.
    - User asks for optimization suggestions.
    - User wants best practice recommendations.

    Args:
        query (str): Source code or code review request.

    Returns:
        str: Detailed code review feedback and recommendations.
    """
    return f"Code Reviewer Tool Activated.\n\nCode Review Request: {query}"


@tool("Debugger")
def Debugger(query: str):
    """
    Tool Name: Debugger

    Use this tool to identify, analyze, and resolve errors in source code.

    When to use:
    - User reports an error or exception.
    - User wants help fixing a bug.
    - User provides stack traces or error messages.
    - User requests debugging assistance.

    Args:
        query (str): Source code, error message, or debugging request.

    Returns:
        str: Debugging analysis, identified issues, and suggested fixes.
    """
    return f"Debugger Tool Activated.\n\nDebugging Request: {query}"