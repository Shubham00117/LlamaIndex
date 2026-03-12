"""
Topic 3 — Text Chunking & Ingestion
Subtopic #13: Node Parsers — Chunking Strategies

Beyond basic splitters, LlamaIndex has specialized node parsers
for different document types and retrieval strategies.

| Parser                  | Best For                | Key Feature                        |
|-------------------------|-------------------------|------------------------------------|
| SentenceSplitter        | General text, articles  | Respects sentence boundaries       |
| TokenTextSplitter       | Code, structured data   | Strict token-count splitting       |
| HierarchicalNodeParser  | Parent-child retrieval  | Creates chunk hierarchy (512→128)  |
| MarkdownNodeParser      | Markdown docs           | Splits on headers (H1, H2, H3)    |
| JSONNodeParser          | JSON / API responses    | Splits on JSON structure           |
| CodeSplitter            | Source code files       | Uses AST — respects function scope |

⚠️ Requires: pip install llama-index-core
"""

from llama_index.core.schema import Document


def hierarchical_node_parser_example():
    """Create a hierarchy of parent and child chunks."""
    
    from llama_index.core.node_parser import HierarchicalNodeParser
    
    doc = Document(
        text=(
            "Chapter 1: Introduction to RAG. "
            "RAG stands for Retrieval Augmented Generation. "
            "It combines retrieval systems with language models. "
            "The retrieval component finds relevant context. "
            "The generation component produces answers. "
            "This pattern is widely used in production. "
            "Chapter 2: Vector Stores. "
            "Vector stores hold embeddings for fast similarity search. "
            "Popular options include Pinecone, Qdrant, and ChromaDB. "
            "Each has different tradeoffs for scale and features. "
        )
    )
    
    # Creates parent chunks (512) and child chunks (256, 128)
    parser = HierarchicalNodeParser.from_defaults(
        chunk_sizes=[512, 256, 128]   # Large → medium → small
    )
    
    nodes = parser.get_nodes_from_documents([doc])
    
    print("=" * 60)
    print("  HierarchicalNodeParser Results")
    print("=" * 60)
    print(f"  Total nodes: {len(nodes)}")
    
    for i, node in enumerate(nodes):
        # Determine level based on text length
        level = "Large" if len(node.text) > 200 else "Medium" if len(node.text) > 100 else "Small"
        print(f"\n  📦 Node {i + 1} [{level}]:")
        print(f"     Text: {node.text[:60]}...")
        print(f"     Length: {len(node.text)} chars")
    
    print("\n💡 Use with AutoMergingRetriever (Topic 8 #47)")
    print("   Retrieve small chunks → return their large parent context to LLM")
    
    return nodes


def markdown_node_parser_example():
    """Split markdown documents on header boundaries."""
    
    from llama_index.core.node_parser import MarkdownNodeParser
    
    doc = Document(
        text=(
            "# Introduction\n\n"
            "This is the introduction section.\n\n"
            "## Getting Started\n\n"
            "Here's how to get started with the project.\n\n"
            "## Installation\n\n"
            "Install using pip:\n"
            "```\npip install my-package\n```\n\n"
            "# Advanced Topics\n\n"
            "These are advanced features.\n\n"
            "## Configuration\n\n"
            "Configure using environment variables.\n"
        )
    )
    
    parser = MarkdownNodeParser()
    nodes = parser.get_nodes_from_documents([doc])
    
    print("\n" + "=" * 60)
    print("  MarkdownNodeParser Results")
    print("=" * 60)
    print(f"  Total nodes: {len(nodes)}")
    
    for i, node in enumerate(nodes):
        print(f"\n  📦 Node {i + 1}:")
        print(f"     Text: {node.text[:60]}...")
    
    return nodes


def show_parser_reference():
    """Display reference of all node parsers."""
    
    print("\n" + "=" * 60)
    print("  Node Parser Reference")
    print("=" * 60)
    
    parsers = {
        "SentenceSplitter": ("General text, articles", "Respects sentence boundaries"),
        "TokenTextSplitter": ("Code, structured data", "Strict token-count splitting"),
        "HierarchicalNodeParser": ("Parent-child retrieval", "Creates chunk hierarchy"),
        "MarkdownNodeParser": ("Markdown docs", "Splits on headers (H1, H2, H3)"),
        "JSONNodeParser": ("JSON / API responses", "Splits on JSON structure"),
        "CodeSplitter": ("Source code files", "Uses AST — respects function scope"),
    }
    
    for name, (best_for, feature) in parsers.items():
        print(f"\n  📋 {name}")
        print(f"     Best for:   {best_for}")
        print(f"     Feature:    {feature}")
    
    print("\n🏆 Best Production Pattern:")
    print("   HierarchicalNodeParser + AutoMergingRetriever")
    print("   → Retrieve small precise chunks, return large parent context")


if __name__ == "__main__":
    hierarchical_node_parser_example()
    markdown_node_parser_example()
    show_parser_reference()
