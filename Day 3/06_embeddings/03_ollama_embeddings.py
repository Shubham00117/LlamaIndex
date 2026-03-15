"""
Topic 6 — Embeddings
Subtopics #29-32: Ollama Embeddings & Custom Models

Ollama embeddings are fully local and offline — no internet required.

⚠️ Requires: pip install llama-index-embeddings-ollama
⚠️ Requires: Ollama running locally (https://ollama.ai)
"""


def setup_ollama_embeddings():
    """Configure Ollama embeddings (fully offline)."""
    
    code = '''
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import Settings

# Make sure Ollama is running and the model is pulled:
#   ollama pull nomic-embed-text

embed_model = OllamaEmbedding(
    model_name="nomic-embed-text",  # Good quality, fast
    base_url="http://localhost:11434",
)

Settings.embed_model = embed_model
'''
    
    print("=" * 60)
    print("  Ollama Embeddings (Fully Offline)")
    print("=" * 60)
    print(code)


def embedding_choice_guide():
    """Guide for choosing the right embedding model."""
    
    print("\n" + "=" * 60)
    print("  Choosing the Right Embedding Model")
    print("=" * 60)
    
    guide = {
        "OpenAI text-embedding-3-small": {
            "Quality": "★★★★☆",
            "Cost": "$ (cheapest cloud)",
            "Speed": "Fast (API call)",
            "When": "Default choice for most projects",
        },
        "HuggingFace bge-base-en-v1.5": {
            "Quality": "★★★★☆",
            "Cost": "FREE",
            "Speed": "Medium (local compute)",
            "When": "Cost-sensitive, data privacy required",
        },
        "Ollama nomic-embed-text": {
            "Quality": "★★★☆☆",
            "Cost": "FREE",
            "Speed": "Fast (local)",
            "When": "Fully offline/air-gapped environments",
        },
        "Cohere embed-english-v3.0": {
            "Quality": "★★★★★",
            "Cost": "$$",
            "Speed": "Fast (API call)",
            "When": "Highest quality needed, multilingual",
        },
    }
    
    for model, details in guide.items():
        print(f"\n  📊 {model}")
        for key, value in details.items():
            print(f"    {key:10s} {value}")
    
    print("\n💡 Key dimensions to consider:")
    print("  • Embedding dimension (must match vector store config)")
    print("  • Similarity metric (cosine is standard)")
    print("  • Cost per million tokens")
    print("  • Latency requirements")


if __name__ == "__main__":
    setup_ollama_embeddings()
    embedding_choice_guide()
