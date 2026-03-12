"""
Topic 4 — Indexing
Subtopic #14: VectorStoreIndex — Core RAG Index

The most-used index in LlamaIndex. It takes your nodes, embeds them,
and stores them in a vector store. At query time, it embeds the question
and finds the most similar nodes via cosine similarity.

Flow: Documents → Nodes (chunks) → Embed → VectorStore → QueryEngine

⚠️ Requires: pip install llama-index-core llama-index-llms-openai llama-index-embeddings-openai
"""

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.schema import Document


def build_from_documents():
    """Build an index directly from documents (simplest approach)."""
    
    # Create sample documents
    documents = [
        Document(text="LlamaIndex is a data framework for LLM-powered applications."),
        Document(text="RAG retrieves relevant context and feeds it to an LLM."),
        Document(text="Vector stores hold embeddings for fast similarity search."),
    ]
    
    # This single line: chunks → embeds → stores → creates index
    index = VectorStoreIndex.from_documents(documents)
    
    # Create a query engine from the index
    query_engine = index.as_query_engine()
    
    print("✅ Index built from documents")
    print(f"   Number of documents: {len(documents)}")
    
    return index, query_engine


def build_from_nodes():
    """Build index from pre-processed nodes (after IngestionPipeline)."""
    
    from llama_index.core.schema import TextNode
    
    # Pre-processed nodes (e.g., from IngestionPipeline)
    nodes = [
        TextNode(text="Chunk 1: LlamaIndex basics...", metadata={"topic": "intro"}),
        TextNode(text="Chunk 2: Vector store integration...", metadata={"topic": "stores"}),
    ]
    
    # Build index from nodes directly
    index = VectorStoreIndex(nodes)
    
    print("✅ Index built from pre-processed nodes")
    return index


def build_from_vector_store():
    """Connect to an existing external vector store."""
    
    # Pattern for connecting to an existing vector store
    code = '''
# When using an external vector store (e.g., Qdrant, Pinecone)
# The data already exists in the store — no need to re-embed

from llama_index.core import VectorStoreIndex

# Just connect to the existing store
index = VectorStoreIndex.from_vector_store(vector_store)
query_engine = index.as_query_engine()
'''
    
    print("\n📋 Pattern for connecting to existing vector store:")
    print(code)


def query_the_index():
    """Build and query an index end-to-end."""
    
    documents = [
        Document(text="Python is a popular programming language for AI and machine learning."),
        Document(text="LlamaIndex connects LLMs with private data sources using RAG."),
        Document(text="Vector databases store numerical representations of text for similarity search."),
    ]
    
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    
    # Query the index
    response = query_engine.query("What is LlamaIndex?")
    
    print("\n" + "=" * 60)
    print("  Query Results")
    print("=" * 60)
    print(f"  Question: What is LlamaIndex?")
    print(f"  Answer: {response}")
    print(f"\n  Source nodes: {len(response.source_nodes)}")
    for node in response.source_nodes:
        print(f"    - Score: {node.score:.4f} | {node.text[:50]}...")


if __name__ == "__main__":
    print("=" * 60)
    print("  VectorStoreIndex — Core RAG Index")
    print("=" * 60)
    
    # Show the patterns
    build_from_vector_store()
    
    print("\n💡 from_documents() is great for prototyping.")
    print("   In production, use an external vector store (Topic 5).")
    
    # Uncomment to run (requires OPENAI_API_KEY):
    # build_from_documents()
    # query_the_index()
