"""
Topic 6 — Embeddings
Subtopic #28: HuggingFace Local Embeddings

HuggingFace embeddings run locally — no API costs.
Great for cost-sensitive projects or when data can't leave your machine.

⚠️ Requires: pip install llama-index-embeddings-huggingface
"""


def setup_huggingface_embeddings():
    """Configure HuggingFace local embeddings."""
    
    from llama_index.embeddings.huggingface import HuggingFaceEmbedding
    from llama_index.core import Settings
    
    # BAAI/bge-small-en-v1.5 — fast, good quality
    embed_model = HuggingFaceEmbedding(
        model_name="BAAI/bge-small-en-v1.5"  # Downloads on first use
    )
    
    # Other good options:
    # "BAAI/bge-base-en-v1.5"  → Better quality, larger
    # "BAAI/bge-large-en-v1.5" → Best quality, largest
    # "sentence-transformers/all-MiniLM-L6-v2" → Very fast, smaller
    
    Settings.embed_model = embed_model
    
    print("✅ HuggingFace Embeddings configured (local)")
    print("   Model: BAAI/bge-small-en-v1.5")
    print("   💰 Cost: FREE — runs entirely on your machine")
    
    return embed_model


if __name__ == "__main__":
    print("=" * 60)
    print("  HuggingFace Local Embeddings")
    print("=" * 60)
    
    print("\n📋 Recommended models:")
    print("  bge-small-en-v1.5  → Fast, good quality (384 dims)")
    print("  bge-base-en-v1.5   → Better quality (768 dims)")
    print("  bge-large-en-v1.5  → Best quality (1024 dims)")
    print("  all-MiniLM-L6-v2   → Very fast, lightweight")
    
    # Uncomment to run:
    # setup_huggingface_embeddings()
