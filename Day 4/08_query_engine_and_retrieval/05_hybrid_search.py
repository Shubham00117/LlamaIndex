"""
Topic 8 — Query Engine & Retrieval
Subtopic #46: Hybrid Search — BM25 + Vector Combined

Hybrid search combines the best of both worlds:
  - BM25 for exact keyword matching
  - Vector for semantic similarity

⚠️ Requires: pip install llama-index-core llama-index-retrievers-bm25
"""


def hybrid_search_example():
    """Set up hybrid search combining BM25 + vector retrieval."""
    
    code = '''
from llama_index.core.retrievers import QueryFusionRetriever
from llama_index.retrievers.bm25 import BM25Retriever

# Create individual retrievers
vector_retriever = index.as_retriever(similarity_top_k=5)
bm25_retriever = BM25Retriever.from_defaults(nodes=nodes, similarity_top_k=5)

# Combine into hybrid retriever
hybrid_retriever = QueryFusionRetriever(
    retrievers=[vector_retriever, bm25_retriever],
    similarity_top_k=5,    # Final top-k after fusion
    num_queries=1,          # Don't generate sub-queries
    mode="reciprocal_rerank",  # Rank fusion algorithm
)

# Use in query engine
from llama_index.core.query_engine import RetrieverQueryEngine

query_engine = RetrieverQueryEngine(retriever=hybrid_retriever)
response = await query_engine.aquery("financial report Q3")
'''
    
    print("=" * 60)
    print("  Hybrid Search — BM25 + Vector")
    print("=" * 60)
    print(code)
    print("🔍 Hybrid search catches both:")
    print("   • Exact terms (BM25): 'Q3 2024 revenue'")
    print("   • Semantic meaning (Vector): 'financial performance'")


if __name__ == "__main__":
    hybrid_search_example()
