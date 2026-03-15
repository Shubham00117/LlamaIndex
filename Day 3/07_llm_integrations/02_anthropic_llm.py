"""
Topic 7 — LLM Integrations
Subtopic #34: Anthropic (Claude)

Anthropic Claude offers long context windows (200K tokens).
Great for processing large documents in a single query.

⚠️ Requires: pip install llama-index-llms-anthropic
"""


def setup_anthropic():
    """Configure Anthropic Claude as the LLM."""
    
    code = '''
from llama_index.llms.anthropic import Anthropic
from llama_index.core import Settings

llm = Anthropic(
    model="claude-sonnet-4-20250514",
    temperature=0.1,
    max_tokens=4096,
)

Settings.llm = llm

# Claude supports 200K token context window
# Great for full document analysis
response = llm.complete("Explain RAG in one sentence.")
'''
    
    print("=" * 60)
    print("  Anthropic Claude Integration")
    print("=" * 60)
    print(code)
    print("💡 Claude's 200K context is great for large document analysis.")


if __name__ == "__main__":
    setup_anthropic()
