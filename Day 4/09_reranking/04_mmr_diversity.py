"""
Topic 9 — Re-ranking
Subtopic #56: MMR (Maximum Marginal Relevance)

MMR ensures diversity in retrieved results by penalizing nodes
that are too similar to already-selected nodes.

Prevents: getting 5 results that all say the same thing.

⚠️ Requires: pip install llama-index-core
"""


def mmr_example():
    """Use MMR for diverse retrieval."""
    
    code = '''
# Use MMR directly in the vector retriever
retriever = index.as_retriever(
    similarity_top_k=5,
    vector_store_query_mode="mmr",  # Enable MMR
    vector_store_kwargs={
        "mmr_threshold": 0.5,  # 0 = max diversity, 1 = max relevance
    },
)

# Or as a post-processor
from llama_index.core.postprocessor import SimilarityPostprocessor

# Filter out nodes below a similarity threshold
postprocessor = SimilarityPostprocessor(similarity_cutoff=0.7)

query_engine = index.as_query_engine(
    similarity_top_k=10,
    node_postprocessors=[postprocessor],
)
'''
    
    print("=" * 60)
    print("  MMR — Maximum Marginal Relevance")
    print("=" * 60)
    print(code)
    print("🎯 MMR balances relevance vs diversity.")
    print("   mmr_threshold=0.5 is a good starting point.")


if __name__ == "__main__":
    mmr_example()
