from langchain.tools import tool
from langchain.agents import create_agent
from src.ultis import get_groq_model, get_system_prompt
from src.tools.Coding_Agent_tools import Code_Generator,Code_Reviewer,Debugger

@tool
def get_code_agents(query : str)->str:
    """
    Coding Agent

    A specialized AI agent designed to assist with software development
    tasks by intelligently selecting from the following tools:

    Available Tools:
    1. Code_Generator
       - Generates source code based on user requirements.
       - Used when users request implementations, functions, classes,
         scripts, APIs, or code examples in any programming language.

    2. Code_Reviewer
       - Reviews existing source code and provides feedback.
       - Used for code quality analysis, best practices, performance
         improvements, readability enhancements, and optimization suggestions.

    3. Debugger
       - Identifies and resolves issues in source code.
       - Used when users provide errors, exceptions, stack traces,
         unexpected behavior, or bug-fixing requests.

    Agent Responsibilities:
    - Analyze the user's request.
    - Select the most appropriate tool based on intent.
    - Generate code when implementation is requested.
    - Review code when feedback or improvements are requested.
    - Debug code when errors or issues are reported.
    - Return clear, actionable, and developer-friendly responses.

    Returns:
        AgentExecutor: Configured coding agent capable of generating,
        reviewing, and debugging code.
    """
    coding_agent = create_agent(
        model=get_groq_model(),
        tools=[Code_Generator, Code_Reviewer,Debugger],
        system_prompt=get_system_prompt("testing")
    )
    result = coding_agent.invoke({"messages" : [{"role" :"user", "content":query}]})
    return result["messages"][-1].content