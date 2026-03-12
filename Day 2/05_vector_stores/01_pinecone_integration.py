"""
Topic 5 — Vector Stores
Subtopic #19: Pinecone Integration

Pinecone is a fully managed cloud vector database.
Best for: teams that want zero infrastructure management.

Pattern: create client → create vector_store → wrap in StorageContext → build index

⚠️ Requires: pip install llama-index-vector-stores-pinecone pinecone-client
"""


def pinecone_setup():
    """Set up Pinecone vector store with LlamaIndex."""
    
    code = '''
from pinecone import Pinecone
from llama_index.vector_stores.pinecone import PineconeVectorStore
from llama_index.core import StorageContext, VectorStoreIndex

# Step 1: Create Pinecone client
pc = Pinecone(api_key="YOUR_PINECONE_API_KEY")

# Step 2: Get your index (must be pre-created in Pinecone dashboard)
pc_index = pc.Index("my-index")

# Step 3: Wrap in LlamaIndex vector store
vector_store = PineconeVectorStore(
    pinecone_index=pc_index
)

# Step 4: Create storage context
storage_ctx = StorageContext.from_defaults(
    vector_store=vector_store
)

# Step 5: Build index (embeds and stores in Pinecone)
index = VectorStoreIndex.from_documents(
    documents,
    storage_context=storage_ctx
)

# Step 6: Query!
query_engine = index.as_query_engine()
response = await query_engine.aquery("What is RAG?")
'''
    
    print("=" * 60)
    print("  Pinecone Integration")
    print("=" * 60)
    print(code)
    print("💡 Pinecone is fully managed — no server to maintain.")
    print("   Create your index at: https://app.pinecone.io")


if __name__ == "__main__":
    pinecone_setup()
