"""
Topic 1 — Setup & Project Foundation
Subtopic #2: Settings Configuration

Settings is a GLOBAL SINGLETON in LlamaIndex.
Set it ONCE at startup — all indexes, query engines, and pipelines
pick it up automatically. No need to pass LLM/embed objects everywhere.

Key settings:
  - Settings.llm          → LLM used for generation, reranking, agents
  - Settings.embed_model  → Embedding model for indexing and querying
  - Settings.chunk_size   → Token size per chunk (default: 1024)
  - Settings.chunk_overlap→ Overlap between chunks (avoids cutting context)

⚠️ Requires: pip install llama-index-core llama-index-llms-openai llama-index-embeddings-openai
⚠️ Set OPENAI_API_KEY environment variable before running.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file (if it exists)
load_dotenv()


def configure_settings_openai():
    """Configure LlamaIndex Settings with OpenAI models."""
    
    from llama_index.core import Settings
    from llama_index.llms.openai import OpenAI
    from llama_index.embeddings.openai import OpenAIEmbedding
    
    # --- Set global LLM ---
    # This LLM is used by query engines, chat engines, agents, etc.
    Settings.llm = OpenAI(
        model="gpt-4o",           # Model to use
        temperature=0.1,          # Low temp = more deterministic answers
    )
    
    # --- Set global embedding model ---
    # Used during indexing (to embed chunks) and querying (to embed questions)
    Settings.embed_model = OpenAIEmbedding(
        model="text-embedding-3-small"  # Cost-effective, good quality
    )
    
    # --- Chunk settings ---
    # These control how documents are split into nodes
    Settings.chunk_size = 512     # Tokens per chunk — good default for RAG
    Settings.chunk_overlap = 50   # Overlap avoids cutting context at boundaries
    
    print("✅ Settings configured with OpenAI GPT-4o + text-embedding-3-small")
    print(f"   Chunk size: {Settings.chunk_size}")
    print(f"   Chunk overlap: {Settings.chunk_overlap}")
    
    return Settings


def configure_settings_local():
    """Configure Settings for fully local/offline usage with Ollama."""
    
    from llama_index.core import Settings
    
    # For local usage, you'd use Ollama (requires Ollama to be running)
    # pip install llama-index-llms-ollama llama-index-embeddings-ollama
    
    try:
        from llama_index.llms.ollama import Ollama
        from llama_index.embeddings.ollama import OllamaEmbedding
        
        Settings.llm = Ollama(model="llama3.2", request_timeout=120)
        Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")
        Settings.chunk_size = 512
        Settings.chunk_overlap = 50
        
        print("✅ Settings configured with Ollama (fully local)")
    except ImportError:
        print("⚠️  Ollama packages not installed.")
        print("   pip install llama-index-llms-ollama llama-index-embeddings-ollama")


def show_settings_explained():
    """Print a reference of key Settings attributes and their meanings."""
    
    print("\n" + "=" * 60)
    print("  LlamaIndex Settings Reference")
    print("=" * 60)
    
    settings_table = {
        "Settings.llm": "The LLM used for generation, reranking, and agents",
        "Settings.embed_model": "Embedding model used during indexing and querying",
        "Settings.chunk_size": "Token size per chunk — smaller = precise, larger = context-rich",
        "Settings.chunk_overlap": "Overlap between chunks — avoids cutting off context",
        "Settings.num_output": "Max output tokens for the LLM response",
        "Settings.context_window": "Max context window size for the LLM",
    }
    
    for key, description in settings_table.items():
        print(f"\n  📌 {key}")
        print(f"     {description}")
    
    print("\n💡 TIP: Start with chunk_size=512, overlap=50 for most RAG projects.")
    print("   Tune based on evaluation results later.")


if __name__ == "__main__":
    show_settings_explained()
    
    # Try configuring with OpenAI (most common setup)
    if os.getenv("OPENAI_API_KEY"):
        configure_settings_openai()
    else:
        print("\n⚠️  OPENAI_API_KEY not set. Showing local config option instead.")
        configure_settings_local()
