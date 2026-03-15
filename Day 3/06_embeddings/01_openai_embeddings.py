"""
Topic 6 — Embeddings
Subtopic #27: OpenAI Embeddings

OpenAI provides the most widely used embedding models.
text-embedding-3-small is cost-effective; text-embedding-3-large is higher quality.

⚠️ Requires: pip install llama-index-embeddings-openai
"""

from llama_index.core import Settings


def setup_openai_embeddings():
    """Configure OpenAI embeddings globally."""
    
    from llama_index.embeddings.openai import OpenAIEmbedding
    
    # Option 1: Cost-effective (recommended default)
    embed_model = OpenAIEmbedding(model="text-embedding-3-small")
    
    # Option 2: Higher quality (for critical applications)
    # embed_model = OpenAIEmbedding(model="text-embedding-3-large")
    
    # Option 3: Reduced dimensions (faster, cheaper)
    # embed_model = OpenAIEmbedding(
    #     model="text-embedding-3-small",
    #     dimensions=256  # Reduce from 1536 to 256
    # )
    
    # Set globally
    Settings.embed_model = embed_model
    
    print("✅ OpenAI Embeddings configured")
    print(f"   Model: {embed_model.model_name}")
    
    # Generate an embedding for a sample text
    embedding = embed_model.get_text_embedding("What is LlamaIndex?")
    print(f"   Embedding dimension: {len(embedding)}")
    print(f"   First 5 values: {embedding[:5]}")
    
    return embed_model


if __name__ == "__main__":
    print("=" * 60)
    print("  OpenAI Embeddings")
    print("=" * 60)
    
    print("\n📋 Models available:")
    print("  text-embedding-3-small → 1536 dims, cheapest")
    print("  text-embedding-3-large → 3072 dims, highest quality")
    print("  text-embedding-ada-002 → 1536 dims, legacy")
    
    # Uncomment to run (requires OPENAI_API_KEY):
    # setup_openai_embeddings()
