"""
Topic 12 — Agents
Subtopics #67-74: ReAct, FunctionCalling, Tools, Memory, Multi-Agent

Agents are autonomous LLM-powered decision makers.
They reason about which tools to use, call them, and iterate.

⚠️ Requires: pip install llama-index-core llama-index-llms-openai
"""

from llama_index.core.tools import FunctionTool


# ─── Define custom tools ───
def multiply(a: int, b: int) -> int:
    """Multiply two integers and return the result."""
    return a * b


def add(a: int, b: int) -> int:
    """Add two integers and return the result."""
    return a + b


def agent_examples():
    """Show agent creation patterns."""
    
    react_code = '''
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool, QueryEngineTool

# Create tools
multiply_tool = FunctionTool.from_defaults(fn=multiply)
add_tool = FunctionTool.from_defaults(fn=add)

# Query engine tool (RAG as a tool)
rag_tool = QueryEngineTool.from_defaults(
    query_engine=query_engine,
    name="knowledge_base",
    description="Searches the knowledge base for information",
)

# Create ReAct agent
agent = ReActAgent.from_tools(
    tools=[multiply_tool, add_tool, rag_tool],
    llm=llm,
    verbose=True,  # Shows reasoning steps
)

# Run the agent
response = await agent.achat("What is 15 * 23, and search the KB for RAG info")
'''
    
    function_calling = '''
from llama_index.core.agent import FunctionCallingAgent

# Uses OpenAI function calling (parallel tool execution)
agent = FunctionCallingAgent.from_tools(
    tools=[multiply_tool, add_tool],
    llm=llm,
    verbose=True,
)
'''
    
    custom_tool = '''
from llama_index.core.tools import FunctionTool

# Create a tool from any Python function
def search_database(query: str, limit: int = 10) -> str:
    """Search the internal database for records."""
    # Your database logic here
    return f"Found {limit} results for: {query}"

db_tool = FunctionTool.from_defaults(
    fn=search_database,
    name="database_search",
    description="Searches the internal database for records",
)
'''
    
    multi_agent = '''
# Multi-agent: agents calling other agents
research_agent = ReActAgent.from_tools([rag_tool], llm=llm)
math_agent = ReActAgent.from_tools([multiply_tool, add_tool], llm=llm)

# Wrap agents as tools for a coordinator agent
from llama_index.core.tools import QueryEngineTool

research_tool = QueryEngineTool.from_defaults(
    query_engine=research_agent,
    name="researcher",
    description="For research and knowledge questions",
)

coordinator = ReActAgent.from_tools(
    tools=[research_tool],
    llm=llm,
)
'''
    
    print("=" * 60)
    print("  LlamaIndex Agents")
    print("=" * 60)
    print("\n🤖 ReAct Agent:")
    print(react_code)
    print("🤖 Function Calling Agent:")
    print(function_calling)
    print("🔧 Custom Tools:")
    print(custom_tool)
    print("🤖🤖 Multi-Agent Pattern:")
    print(multi_agent)


if __name__ == "__main__":
    agent_examples()
