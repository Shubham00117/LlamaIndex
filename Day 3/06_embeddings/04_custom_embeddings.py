"""
Topic 6 — Embeddings
Subtopic #31: Custom Embedding Models

Build a custom embedding model by subclassing BaseEmbedding.
Useful for proprietary models or custom preprocessing.

⚠️ Requires: pip install llama-index-core
"""

from llama_index.core.embeddings import BaseEmbedding
from typing import List


class MyCustomEmbedding(BaseEmbedding):
    """
    Example custom embedding model.
    Replace the embedding logic with your actual model.
    """
    
    def __init__(self, model_name: str = "custom-v1", **kwargs):
        super().__init__(model_name=model_name, **kwargs)
    
    def _get_text_embedding(self, text: str) -> List[float]:
        """Generate embedding for a single text."""
        # Replace with your actual embedding logic
        # e.g., calling a custom API or local model
        import hashlib
        hash_val = hashlib.sha256(text.encode()).hexdigest()
        # Dummy: convert hash to a list of floats
        return [int(c, 16) / 15.0 for c in hash_val[:128]]
    
    def _get_query_embedding(self, query: str) -> List[float]:
        """Generate embedding for a query (may differ from text)."""
        return self._get_text_embedding(query)
    
    async def _aget_text_embedding(self, text: str) -> List[float]:
        """Async version of text embedding."""
        return self._get_text_embedding(text)
    
    async def _aget_query_embedding(self, query: str) -> List[float]:
        """Async version of query embedding."""
        return self._get_query_embedding(query)


if __name__ == "__main__":
    print("=" * 60)
    print("  Custom Embedding Model")
    print("=" * 60)
    
    embed_model = MyCustomEmbedding()
    embedding = embed_model._get_text_embedding("Hello world")
    
    print(f"  Embedding dimension: {len(embedding)}")
    print(f"  First 5 values: {embedding[:5]}")
    print("\n💡 Subclass BaseEmbedding and implement:")
    print("   _get_text_embedding() and _get_query_embedding()")
