from langchain.tools import tool


@tool("Code_Generator")
def codegenerator(query: str) -> str:
    """
    Generate new code from a user requirement.

    Use ONLY when the user asks to:
    - create code
    - write code
    - generate code
    - build a program

    Do NOT use for:
    - code review
    - debugging
    - bug fixing

    Return the generated code and stop.
    """
    return f"Code Generation Request: {query}"


@tool("Code_Reviewer")
def codereviewer(query: str) -> str:
    """
    Review existing code and provide feedback.

    Use ONLY when the user provides code and asks for:
    - review
    - optimization
    - refactoring
    - best practices
    - quality improvements

    Do NOT use for:
    - generating new code
    - debugging runtime errors

    Return review feedback and stop.
    """
    return f"Code Review Request: {query}"


@tool("Debugger")
def debugger(query: str) -> str:
    """
    Analyze errors, bugs, logs, or stack traces.

    Use ONLY when the user provides:
    - an error message
    - a stack trace
    - failing code
    - bug reports
    - logs

    Do NOT use for:
    - code generation
    - code review

    Return the root cause and suggested fix, then stop.
    """
    return f"Debugging Request: {query}"