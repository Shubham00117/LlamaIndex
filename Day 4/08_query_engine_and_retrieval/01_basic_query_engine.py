"""
Topic 8 — Query Engine & Retrieval
Subtopic #41: Basic Query Engine & Response Modes

The Query Engine is created from an index. It handles:
  1. Embed the question
  2. Retrieve top-k similar nodes
  3. Feed nodes + question to LLM
  4. Return response

Response modes control HOW the LLM processes retrieved nodes:
  - compact     → Stuff all nodes in one prompt (default, fast)
  - refine      → Process nodes one by one, refining the answer
  - tree_summarize → Build a summary tree bottom-up

⚠️ Requires: pip install llama-index-core llama-index-llms-openai
"""


def query_engine_modes():
    """Show different response modes."""
    
    code = '''
from llama_index.core import VectorStoreIndex

# Build index (assuming documents are loaded)
index = VectorStoreIndex.from_documents(documents)

# Mode 1: compact (default) — fastest, good for simple Q&A
query_engine = index.as_query_engine(
    response_mode="compact",
    similarity_top_k=3,  # Retrieve top 3 similar chunks
)

# Mode 2: refine — processes nodes iteratively, best for complex answers
query_engine = index.as_query_engine(
    response_mode="refine",
    similarity_top_k=5,
)

# Mode 3: tree_summarize — builds summary tree, best for summarization
query_engine = index.as_query_engine(
    response_mode="tree_summarize",
    similarity_top_k=10,
)

# Query
response = await query_engine.aquery("What are the key findings?")
print(response)

# Access source nodes
for node in response.source_nodes:
    print(f"  Score: {node.score:.4f}")
    print(f"  Text: {node.text[:80]}...")
'''
    
    print("=" * 60)
    print("  Query Engine Response Modes")
    print("=" * 60)
    print(code)
    
    print("📋 Response Modes:")
    print("  compact        → Stuff all nodes in one prompt (fast)")
    print("  refine         → Iteratively refine answer (thorough)")
    print("  tree_summarize → Build summary tree (best for summaries)")
    print("  no_text        → Return only retrieved nodes, no LLM")
    print("  accumulate     → Separate LLM call per node, accumulate")


if __name__ == "__main__":
    query_engine_modes()
