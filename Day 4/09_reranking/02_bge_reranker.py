"""
Topic 9 — Re-ranking
Subtopic #54: BGE Reranker (Local)

BGE Reranker runs locally — no API costs, no data leaves your machine.
Good quality reranking using a cross-encoder model.

⚠️ Requires: pip install llama-index-postprocessor-flag-embedding-reranker
"""


def bge_reranker_example():
    """Set up BGE local reranker."""
    
    code = '''
from llama_index.postprocessor.flag_embedding_reranker import (
    FlagEmbeddingReranker
)

reranker = FlagEmbeddingReranker(
    model="BAAI/bge-reranker-base",  # Downloads on first use
    top_n=5,
)

query_engine = index.as_query_engine(
    similarity_top_k=20,
    node_postprocessors=[reranker],
)
'''
    
    print("=" * 60)
    print("  BGE Reranker (Local)")
    print("=" * 60)
    print(code)
    print("💰 FREE — runs entirely on your machine.")
    print("   Models: bge-reranker-base, bge-reranker-large")


if __name__ == "__main__":
    bge_reranker_example()
