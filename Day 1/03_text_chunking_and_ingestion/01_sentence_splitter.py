"""
Topic 3 — Text Chunking & Ingestion
Subtopic #10: SentenceSplitter & TokenTextSplitter

After loading documents, they must be split into smaller chunks (Nodes)
before embedding. These two splitters are used in almost every project.

SentenceSplitter  → Respects sentence boundaries (preferred for natural text)
TokenTextSplitter → Strict token count (better for code, tables, structured text)

Chunk overlap ensures no context is lost at boundaries.

⚠️ Requires: pip install llama-index-core
"""

from llama_index.core.node_parser import SentenceSplitter, TokenTextSplitter
from llama_index.core.schema import Document


def sentence_splitter_example():
    """Split text respecting sentence boundaries."""
    
    # Create a sample document
    doc = Document(
        text=(
            "LlamaIndex is a data framework for LLM applications. "
            "It provides tools for data ingestion, indexing, and querying. "
            "The main use case is RAG — Retrieval Augmented Generation. "
            "RAG retrieves relevant context from a knowledge base and feeds it to an LLM. "
            "This produces more accurate, grounded answers. "
            "LlamaIndex supports many vector stores like Pinecone, Qdrant, and ChromaDB. "
            "It also supports multiple LLM providers including OpenAI, Anthropic, and Ollama."
        )
    )
    
    # SentenceSplitter — the default choice for natural text
    splitter = SentenceSplitter(
        chunk_size=100,       # Max tokens per chunk
        chunk_overlap=20,     # Overlap between adjacent chunks
    )
    
    # Split into nodes
    nodes = splitter.get_nodes_from_documents([doc])
    
    print("=" * 60)
    print("  SentenceSplitter Results")
    print("=" * 60)
    print(f"  Document length: ~{len(doc.text.split())} words")
    print(f"  Number of chunks: {len(nodes)}")
    
    for i, node in enumerate(nodes):
        print(f"\n  📦 Chunk {i + 1}:")
        print(f"     Text: {node.text[:80]}...")
        print(f"     Approx words: {len(node.text.split())}")
    
    return nodes


def token_text_splitter_example():
    """Split text with strict token count."""
    
    doc = Document(
        text=(
            "def calculate_total(items):\n"
            "    total = 0\n"
            "    for item in items:\n"
            "        total += item.price * item.quantity\n"
            "    return total\n\n"
            "class ShoppingCart:\n"
            "    def __init__(self):\n"
            "        self.items = []\n"
            "    def add_item(self, item):\n"
            "        self.items.append(item)\n"
            "    def get_total(self):\n"
            "        return calculate_total(self.items)\n"
        )
    )
    
    # TokenTextSplitter — strict token-count, better for code
    splitter = TokenTextSplitter(
        chunk_size=50,        # Strict token count per chunk
        chunk_overlap=10,     # Overlap in tokens
    )
    
    nodes = splitter.get_nodes_from_documents([doc])
    
    print("\n" + "=" * 60)
    print("  TokenTextSplitter Results (Code)")
    print("=" * 60)
    print(f"  Number of chunks: {len(nodes)}")
    
    for i, node in enumerate(nodes):
        print(f"\n  📦 Chunk {i + 1}:")
        print(f"     {node.text[:60]}...")
    
    return nodes


def compare_splitters():
    """Show when to use which splitter."""
    
    print("\n" + "=" * 60)
    print("  Splitter Comparison")
    print("=" * 60)
    
    comparison = {
        "SentenceSplitter": {
            "Best for": "Natural text, articles, documentation",
            "Key feature": "Splits on sentence boundaries — never cuts mid-sentence",
            "Default": "Yes — preferred for most RAG projects",
        },
        "TokenTextSplitter": {
            "Best for": "Code, tables, structured text",
            "Key feature": "Strict token count — consistent chunk sizes",
            "Default": "No — use when you need precise token control",
        },
    }
    
    for name, details in comparison.items():
        print(f"\n  📋 {name}:")
        for key, value in details.items():
            print(f"    {key}: {value}")
    
    print("\n💡 Chunk Size Guidelines:")
    print("   128–256 tokens  → Precise retrieval (medical, legal Q&A)")
    print("   512 tokens      → Good default for most RAG use cases")
    print("   1024+ tokens    → Summarization, broad context tasks")
    print("\n✅ Start with: SentenceSplitter(chunk_size=512, chunk_overlap=50)")


if __name__ == "__main__":
    sentence_splitter_example()
    token_text_splitter_example()
    compare_splitters()
