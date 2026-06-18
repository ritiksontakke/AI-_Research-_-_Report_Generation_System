from langchain.tools import tool

@tool("Code_Generator")
def Code_Generator(query: str) -> str:
    """
    Generate source code based on the user's natural language request.

    Args:
        query (str): A description of the code to generate, including
            requirements, functionality, programming language, or any
            specific constraints.

    Returns:
        str: The generated code as a string.
    """
    return f"Code Generation Request: {query}"


@tool("Code_Reviewer")
def Code_Reviewer(query: str) -> str:
    """
    Analyze code and provide a comprehensive review.

    Use this tool when you need to identify bugs, code smells,
    security vulnerabilities, performance bottlenecks, style issues,
    or opportunities for refactoring in a code snippet.

    Args:
        query (str): The code to review and any relevant context.

    Returns:
        str: Review findings, improvement recommendations, and
        suggested code changes.
    """
    return f"Code Review Request: {query}"


@tool("Debugger")
def Debugger(query: str) -> str:
    """
    Diagnose and resolve programming errors.

    Use this tool when code produces errors, fails tests,
    behaves unexpectedly, or requires troubleshooting.
    Analyze the provided code, logs, stack traces, or
    issue description and recommend solutions.

    Args:
        query (str): Code, error output, stack trace, logs,
            or a description of the bug.

    Returns:
        str: Root cause analysis, debugging insights,
        and suggested fixes.
    """
    return f"Debugging Request: {query}"