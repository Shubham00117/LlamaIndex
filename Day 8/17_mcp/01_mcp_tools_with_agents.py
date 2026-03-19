"""
Topic 17 — MCP (Model Context Protocol)
Subtopics #99-101: MCP Tools, MCP Servers, LlamaCloud MCP

MCP enables interoperability between AI tools and agents.

⚠️ Requires: pip install llama-index-tools-mcp
"""


def mcp_examples():
    """Show MCP integration patterns."""
    
    use_mcp = '''
# Use MCP tools with LlamaIndex agents
from llama_index.tools.mcp import BasicMCPClient, McpToolSpec

# Connect to an MCP server
mcp_client = BasicMCPClient("http://localhost:3000")
mcp_tool_spec = McpToolSpec(client=mcp_client)

# Get tools from MCP server
tools = await mcp_tool_spec.to_tool_list_async()

# Use with a LlamaIndex agent
from llama_index.core.agent import ReActAgent

agent = ReActAgent.from_tools(tools=tools, llm=llm, verbose=True)
response = await agent.achat("Use the MCP tools to help me")
'''
    
    as_mcp_server = '''
# Convert LlamaIndex tools/workflows into MCP servers
from llama_index.tools.mcp import MCPServer
from llama_index.core.tools import FunctionTool

# Create your LlamaIndex tools
def search_docs(query: str) -> str:
    """Search the knowledge base."""
    return "Search results..."

tool = FunctionTool.from_defaults(fn=search_docs)

# Serve as MCP server
server = MCPServer(tools=[tool])
server.run(port=3000)
# Now other MCP clients can discover and use your tools!
'''
    
    print("=" * 60)
    print("  MCP — Model Context Protocol")
    print("=" * 60)
    print("\n📡 Using MCP tools with agents:")
    print(use_mcp)
    print("🖥️  Converting LlamaIndex to MCP server:")
    print(as_mcp_server)


if __name__ == "__main__":
    mcp_examples()
