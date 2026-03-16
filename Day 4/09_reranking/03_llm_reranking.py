"""
Topic 9 — Re-ranking
Subtopic #55: LLM-based Reranking

Use your LLM to score relevance of each retrieved node.
Most expensive but highest quality reranking.

⚠️ Requires: pip install llama-index-core
"""


def llm_reranker_example():
    """LLM-based reranking."""
    
    code = '''
from llama_index.core.postprocessor import LLMRerank

reranker = LLMRerank(
    top_n=5,
    choice_batch_size=5,  # Process 5 nodes per LLM call
)

query_engine = index.as_query_engine(
    similarity_top_k=15,
    node_postprocessors=[reranker],
)
'''
    
    print("=" * 60)
    print("  LLM-based Reranking")
    print("=" * 60)
    print(code)
    print("⚠️  Most expensive — calls LLM per batch of nodes.")
    print("   Use when quality matters more than cost.")


if __name__ == "__main__":
    llm_reranker_example()
