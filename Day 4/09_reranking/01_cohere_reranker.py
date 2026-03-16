"""
Topic 9 — Re-ranking
Subtopic #53: Cohere Reranker

Re-ranking re-orders retrieved nodes by relevance AFTER initial retrieval.
Cohere's reranker is the most popular production choice.

Flow: Query → Retrieve top-20 → Rerank → Keep top-5 → Send to LLM

⚠️ Requires: pip install llama-index-postprocessor-cohere-rerank
"""


def cohere_reranker_example():
    """Set up Cohere reranker as a post-processor."""
    
    code = '''
from llama_index.postprocessor.cohere_rerank import CohereRerank

# Create reranker
reranker = CohereRerank(
    api_key="YOUR_COHERE_KEY",
    top_n=5,    # Keep top 5 after reranking
)

# Use with query engine
query_engine = index.as_query_engine(
    similarity_top_k=20,          # Retrieve 20 candidates
    node_postprocessors=[reranker],  # Rerank down to 5
)

response = await query_engine.aquery("What are the key findings?")
'''
    
    print("=" * 60)
    print("  Cohere Reranker")
    print("=" * 60)
    print(code)
    print("💡 Pattern: retrieve MORE nodes (20), rerank to fewer (5).")
    print("   This catches relevant nodes that might rank low initially.")


if __name__ == "__main__":
    cohere_reranker_example()
