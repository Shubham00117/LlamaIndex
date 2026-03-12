"""
Topic 5 — Vector Stores
Subtopic #20: Qdrant Integration

Qdrant is the most popular open-source vector store.
Features: fast, rich metadata filtering, self-hosted or cloud.

⚠️ Requires: pip install llama-index-vector-stores-qdrant qdrant-client
"""


def qdrant_setup():
    """Set up Qdrant vector store with LlamaIndex."""
    
    code = '''
import qdrant_client
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core import StorageContext, VectorStoreIndex

# Local Qdrant (run: docker run -p 6333:6333 qdrant/qdrant)
client = qdrant_client.QdrantClient(
    url="http://localhost:6333"
    # For cloud: url="https://xxx.qdrant.io", api_key="..."
)

# Create vector store
vector_store = QdrantVectorStore(
    client=client,
    collection_name="my_collection"
)

# Standard pattern: StorageContext → VectorStoreIndex
storage_ctx = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(documents, storage_context=storage_ctx)

# Reconnect to existing collection (no re-embedding)
index = VectorStoreIndex.from_vector_store(vector_store)
'''
    
    print("=" * 60)
    print("  Qdrant Integration")
    print("=" * 60)
    print(code)
    print("💡 Qdrant has the richest metadata filtering of any OSS store.")
    print("   Run locally with Docker or use Qdrant Cloud.")


if __name__ == "__main__":
    qdrant_setup()
