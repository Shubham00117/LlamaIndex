"""
Topic 5 — Vector Stores
Subtopic #22: ChromaDB Integration

ChromaDB is the easiest local vector store — no server needed.
Best for: local development, prototyping, small applications.

⚠️ Requires: pip install llama-index-vector-stores-chroma chromadb
"""

import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext, VectorStoreIndex


def chromadb_persistent():
    """Set up a persistent local ChromaDB store."""
    
    # Persistent local DB — data survives restarts
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    
    # Get or create a collection
    collection = chroma_client.get_or_create_collection("my_documents")
    
    # Wrap in LlamaIndex
    vector_store = ChromaVectorStore(chroma_collection=collection)
    storage_ctx = StorageContext.from_defaults(vector_store=vector_store)
    
    print("✅ ChromaDB persistent store ready at ./chroma_db")
    print("   Data survives app restarts.")
    
    return vector_store, storage_ctx


def chromadb_in_memory():
    """Set up an in-memory ChromaDB store (for testing)."""
    
    # In-memory — data is lost on restart (great for tests)
    chroma_client = chromadb.Client()
    collection = chroma_client.get_or_create_collection("test_collection")
    
    vector_store = ChromaVectorStore(chroma_collection=collection)
    
    print("✅ ChromaDB in-memory store ready (for testing)")
    return vector_store


if __name__ == "__main__":
    print("=" * 60)
    print("  ChromaDB Integration")
    print("=" * 60)
    
    chromadb_persistent()
    chromadb_in_memory()
    
    print("\n💡 ChromaDB is the fastest way to start.")
    print("   Upgrade to Qdrant/Pinecone for production scale.")
