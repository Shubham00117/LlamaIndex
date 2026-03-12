"""
Topic 5 — Vector Stores
Subtopic #21: Weaviate Integration

Weaviate has built-in hybrid search: BM25 (keyword) + vector combined.
No extra configuration needed.

⚠️ Requires: pip install llama-index-vector-stores-weaviate weaviate-client
"""


def weaviate_setup():
    """Set up Weaviate with built-in hybrid search."""
    
    code = '''
import weaviate
from llama_index.vector_stores.weaviate import WeaviateVectorStore
from llama_index.core import StorageContext, VectorStoreIndex

# Connect to local Weaviate (run via Docker)
client = weaviate.connect_to_local()

# Create vector store
vector_store = WeaviateVectorStore(
    weaviate_client=client,
    index_name="MyDocuments"
)

# Standard pattern
storage_ctx = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(documents, storage_context=storage_ctx)
'''
    
    print("=" * 60)
    print("  Weaviate Integration")
    print("=" * 60)
    print(code)
    print("🔍 Weaviate automatically combines keyword + vector search.")
    print("   Great when queries could be keyword OR semantic.")


if __name__ == "__main__":
    weaviate_setup()
