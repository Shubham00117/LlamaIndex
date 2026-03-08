"""
Topic 1 — Setup & Project Foundation
Subtopic #1: Installation & Project Structure

LlamaIndex uses a modular architecture:
  - llama-index-core: Always needed (the foundation)
  - Integration packages: Install only what you use (LLMs, embeddings, vector stores)

Run this file to verify your installation is working.
"""

import subprocess
import sys


def show_install_commands():
    """Display the recommended pip install commands."""
    
    print("=" * 60)
    print("  LlamaIndex — Installation Commands")
    print("=" * 60)
    
    # --- Core package (always needed) ---
    print("\n📦 Core — always needed:")
    print("  pip install llama-index-core")
    
    # --- LLM integration packages (pick your provider) ---
    print("\n🤖 LLM Integrations (pick one or more):")
    print("  pip install llama-index-llms-openai       # OpenAI GPT-4o / GPT-4")
    print("  pip install llama-index-llms-anthropic     # Anthropic Claude")
    print("  pip install llama-index-llms-ollama        # Ollama (local models)")
    
    # --- Embedding integration packages ---
    print("\n🧮 Embedding Integrations:")
    print("  pip install llama-index-embeddings-openai  # OpenAI embeddings")
    print("  pip install llama-index-embeddings-huggingface  # HuggingFace (free)")
    
    # --- Vector store integration packages ---
    print("\n🗄️  Vector Store Integrations:")
    print("  pip install llama-index-vector-stores-qdrant    # Qdrant")
    print("  pip install llama-index-vector-stores-chroma    # ChromaDB (local)")
    print("  pip install llama-index-vector-stores-pinecone  # Pinecone (cloud)")


def show_project_structure():
    """Display the recommended project structure for a RAG application."""
    
    print("\n" + "=" * 60)
    print("  Recommended Project Structure")
    print("=" * 60)
    
    # A clean separation of concerns is key for maintainable RAG apps
    structure = """
    my_rag_app/
    ├── main.py          # Entry point — starts FastAPI or CLI
    ├── ingestion.py     # Document loading + indexing pipeline
    ├── query.py         # Query engine logic and retrieval
    ├── config.py        # Settings, environment variable loading
    ├── data/            # Raw source documents (PDFs, TXT, etc.)
    ├── storage/         # Persisted index files (auto-generated)
    └── .env             # API keys (OPENAI_API_KEY, etc.)
    """
    print(structure)
    
    # Why this structure matters
    print("💡 Key Principles:")
    print("  • Separate ingestion from querying — they run at different times")
    print("  • Keep config centralized — Settings singleton in config.py")
    print("  • Never commit .env — add it to .gitignore")
    print("  • storage/ is auto-generated — can be gitignored too")


def verify_installation():
    """Verify that llama-index-core is installed and importable."""
    
    print("\n" + "=" * 60)
    print("  Verifying Installation")
    print("=" * 60)
    
    try:
        # Try importing the core package
        import llama_index.core
        print(f"\n✅ llama-index-core is installed!")
        print(f"   Version: {llama_index.core.__version__}")
    except ImportError:
        print("\n❌ llama-index-core is NOT installed.")
        print("   Run: pip install llama-index-core")
    
    # Check optional packages
    optional_packages = [
        ("llama_index.llms.openai", "llama-index-llms-openai"),
        ("llama_index.embeddings.openai", "llama-index-embeddings-openai"),
    ]
    
    print("\n📋 Optional Package Check:")
    for module_name, pip_name in optional_packages:
        try:
            __import__(module_name)
            print(f"  ✅ {pip_name}")
        except ImportError:
            print(f"  ⚠️  {pip_name} — not installed (install if needed)")


if __name__ == "__main__":
    show_install_commands()
    show_project_structure()
    verify_installation()
