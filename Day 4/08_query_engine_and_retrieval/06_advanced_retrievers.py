"""
Topic 8 — Query Engine & Retrieval
Subtopics #47-52: Advanced Retrievers

LlamaIndex provides sophisticated retrieval strategies for production:
  - Auto-Merging Retriever    → Hierarchical chunk retrieval
  - Recursive Retriever       → Parent-child chunk strategy
  - Query Fusion Retriever    → Merging multiple retrievers
  - Router Retriever           → Routing queries to different indexes
  - Auto-Retrieval             → Metadata-filtered vector search

⚠️ Requires: pip install llama-index-core
"""


def advanced_retrievers_reference():
    """Show all advanced retriever patterns."""
    
    retrievers = {
        "Auto-Merging Retriever (#47)": '''
# Retrieve small chunks, auto-merge to parent chunk if enough children match
from llama_index.core.retrievers import AutoMergingRetriever
from llama_index.core.node_parser import HierarchicalNodeParser

# First, create hierarchical nodes
parser = HierarchicalNodeParser.from_defaults(chunk_sizes=[512, 256, 128])
nodes = parser.get_nodes_from_documents(documents)

# Build index from leaf nodes, store all nodes in docstore
retriever = AutoMergingRetriever(
    vector_retriever=index.as_retriever(similarity_top_k=6),
    storage_context=index.storage_context,
    verbose=True,
)
''',
        "Recursive Retriever (#48)": '''
# Retrieve small nodes, then fetch their parent nodes for more context
from llama_index.core.retrievers import RecursiveRetriever

retriever = RecursiveRetriever(
    root_id="vector",
    retriever_dict={"vector": vector_retriever},
    node_dict=all_nodes_dict,  # Maps node_id -> node
    verbose=True,
)
''',
        "Router Retriever (#51)": '''
# Route queries to different indexes based on the query content
from llama_index.core.retrievers import RouterRetriever
from llama_index.core.selectors import LLMSingleSelector
from llama_index.core.tools import RetrieverTool

tools = [
    RetrieverTool.from_defaults(
        retriever=finance_retriever,
        description="For finance and accounting queries",
    ),
    RetrieverTool.from_defaults(
        retriever=engineering_retriever,
        description="For engineering and technical queries",
    ),
]

retriever = RouterRetriever(
    selector=LLMSingleSelector.from_defaults(),
    retriever_tools=tools,
)
''',
    }
    
    print("=" * 60)
    print("  Advanced Retrievers")
    print("=" * 60)
    
    for name, code in retrievers.items():
        print(f"\n{'─' * 50}")
        print(f"  🔍 {name}")
        print(f"{'─' * 50}")
        print(code)
    
    print("\n🏆 Most effective production pattern:")
    print("   HierarchicalNodeParser + AutoMergingRetriever")
    print("   Retrieve precise small chunks → return large parent context")


if __name__ == "__main__":
    advanced_retrievers_reference()
