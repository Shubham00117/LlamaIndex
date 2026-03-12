"""
Topic 4 — Indexing
Subtopic #17: Property Graph Index — Knowledge Graph RAG

Instead of just embedding chunks, a Property Graph Index extracts
entities and relationships from documents and builds a knowledge graph.

Enables multi-hop reasoning:
  "Who is the CEO of the company that acquired Acme?"

⚠️ Graph extraction uses many LLM calls — expensive on large corpora.
   Best for: legal, medical, research literature.

⚠️ Requires: pip install llama-index-core llama-index-llms-openai
"""

from llama_index.core.schema import Document


def property_graph_index_example():
    """Create a Property Graph Index from documents."""
    
    code = '''
from llama_index.core import PropertyGraphIndex

# Build the knowledge graph from documents
# LLM extracts entities + relationships automatically
index = PropertyGraphIndex.from_documents(
    documents,
    show_progress=True  # Display extraction progress
)

# Query with graph-aware retrieval
query_engine = index.as_query_engine(
    include_text=True  # Include source text with graph results
)

response = query_engine.query(
    "Who founded the company that created GPT-4?"
)
'''
    
    print("=" * 60)
    print("  Property Graph Index")
    print("=" * 60)
    print(code)
    
    print("📋 How it works:")
    print("  1. LLM reads each document chunk")
    print("  2. Extracts entities (people, companies, products)")
    print("  3. Extracts relationships (founded_by, produces, used_in)")
    print("  4. Builds a traversable knowledge graph")
    print("  5. At query time, traverses graph + retrieves text")
    
    print("\n⚠️  Cost Warning:")
    print("  Graph extraction = many LLM calls per document.")
    print("  Best for complex relationship-heavy domains.")
    
    print("\n🏷️  Use cases:")
    print("  • Legal document analysis")
    print("  • Medical research literature")
    print("  • Corporate organizational knowledge")


if __name__ == "__main__":
    property_graph_index_example()
