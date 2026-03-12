"""
Topic 4 — Indexing
Subtopic #18: Persistent Storage — Save & Load Index

In-memory indexes are lost on restart. Persist them to disk
(or use an external vector DB) so you don't re-embed every time.

What gets saved:
  - docstore.json      → All Document and Node objects
  - index_store.json   → Index metadata and structure
  - vector_store.json  → Embeddings (only for in-memory/SimpleVectorStore)
  - graph_store.json   → Knowledge graph data (if PropertyGraphIndex)

⚠️ Requires: pip install llama-index-core
"""


def save_and_load_example():
    """Show how to persist and reload an index."""
    
    print("=" * 60)
    print("  Persistent Storage — Save & Load Index")
    print("=" * 60)
    
    save_code = '''
from llama_index.core import VectorStoreIndex, StorageContext

# Build index as usual
index = VectorStoreIndex.from_documents(documents)

# Save to disk — creates docstore.json, index_store.json, vector_store.json
index.storage_context.persist(persist_dir="./storage")
'''
    
    load_code = '''
from llama_index.core import load_index_from_storage, StorageContext

# Reload from disk — no re-embedding needed!
storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)

# Use normally
query_engine = index.as_query_engine()
'''
    
    print("\n💾 SAVE index to disk:")
    print(save_code)
    print("📂 LOAD index from disk:")
    print(load_code)
    
    print("📋 Files created in storage directory:")
    print("  docstore.json      → Document and Node objects")
    print("  index_store.json   → Index metadata and structure")
    print("  vector_store.json  → Embeddings (in-memory store only)")
    print("  graph_store.json   → Knowledge graph (PropertyGraphIndex)")
    
    print("\n💡 Production Tip:")
    print("  Skip disk persistence — use an external vector store")
    print("  (Pinecone, Qdrant, etc.) that handles persistence natively.")


if __name__ == "__main__":
    save_and_load_example()
