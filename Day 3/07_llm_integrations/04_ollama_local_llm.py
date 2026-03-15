"""
Topic 7 — LLM Integrations
Subtopic #37: Ollama (Local/Offline Models)

Ollama lets you run LLMs locally — no internet, no API costs.
Great for development, testing, and air-gapped environments.

⚠️ Requires: pip install llama-index-llms-ollama
⚠️ Requires: Ollama installed (https://ollama.ai) and model pulled
"""


def setup_ollama():
    """Configure Ollama for fully local LLM."""
    
    code = '''
from llama_index.llms.ollama import Ollama
from llama_index.core import Settings

# Make sure to pull the model first: ollama pull llama3.2
llm = Ollama(
    model="llama3.2",
    request_timeout=120,  # seconds — local models can be slow
)

Settings.llm = llm

# Test it
response = llm.complete("What is RAG?")
print(response.text)
'''
    
    print("=" * 60)
    print("  Ollama — Local LLM")
    print("=" * 60)
    print(code)
    print("💡 Ollama models: llama3.2, mistral, codellama, phi3")
    print("   Pull with: ollama pull <model-name>")


if __name__ == "__main__":
    setup_ollama()
