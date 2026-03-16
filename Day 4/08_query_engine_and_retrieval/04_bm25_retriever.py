"""
Topic 8 — Query Engine & Retrieval
Subtopic #45: BM25 Retriever — Keyword/Sparse Retrieval

BM25 is a keyword-based retrieval algorithm (like traditional search).
It finds documents by matching exact words, not semantic meaning.

Use BM25 when: queries contain specific terms, names, or codes
that vector search might miss.

⚠️ Requires: pip install llama-index-retrievers-bm25 rank-bm25
"""


def bm25_retriever_example():
    """Set up BM25 keyword retriever."""
    
    code = '''
from llama_index.retrievers.bm25 import BM25Retriever

# Create BM25 retriever from index nodes
bm25_retriever = BM25Retriever.from_defaults(
    nodes=nodes,           # Your processed nodes
    similarity_top_k=5,   # Return top 5 keyword matches
)

# Retrieve by keyword matching
results = bm25_retriever.retrieve("financial report Q3 2024")

for node in results:
    print(f"Score: {node.score:.4f} | {node.text[:60]}...")
'''
    
    print("=" * 60)
    print("  BM25 Keyword Retriever")
    print("=" * 60)
    print(code)
    print("💡 BM25 excels at exact term matching.")
    print("   Combine with vector search for hybrid retrieval.")


if __name__ == "__main__":
    bm25_retriever_example()
