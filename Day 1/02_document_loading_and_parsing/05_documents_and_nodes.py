"""
Topic 2 — Document Loading & Parsing
Subtopic #8: Documents & Nodes

These are the TWO core data structures in LlamaIndex:

  Document  → A full source file (e.g., one PDF)
              Has: .text, .metadata, .doc_id
  
  Node      → A chunk of a Document after splitting
  (TextNode)  This is what actually gets embedded and stored

Understanding these is essential for any LlamaIndex customization.

⚠️ Requires: pip install llama-index-core
"""

from llama_index.core.schema import Document, TextNode, NodeRelationship, RelatedNodeInfo


def create_documents():
    """Create Document objects manually."""
    
    print("=" * 60)
    print("  Creating Documents")
    print("=" * 60)
    
    # --- Create a simple document ---
    doc = Document(
        text="LlamaIndex is a framework for building RAG applications. "
             "It connects your data with LLMs for intelligent retrieval.",
        metadata={
            "source": "docs",
            "author": "team",
            "version": "1.0",
        }
    )
    
    print(f"\n📄 Document:")
    print(f"   doc_id:   {doc.doc_id}")           # Auto-generated UUID
    print(f"   text:     {doc.text[:60]}...")
    print(f"   metadata: {doc.metadata}")
    
    # --- Create with explicit ID ---
    doc_with_id = Document(
        text="Custom document with explicit ID.",
        doc_id="my-custom-doc-001",              # Useful for updates/deletes
        metadata={"source": "manual"}
    )
    
    print(f"\n📄 Document with custom ID: {doc_with_id.doc_id}")
    
    return doc


def create_nodes():
    """Create TextNode objects manually."""
    
    print("\n" + "=" * 60)
    print("  Creating Nodes (TextNode)")
    print("=" * 60)
    
    # --- Create a standalone node ---
    node = TextNode(
        text="LlamaIndex is a framework for building RAG apps.",
        metadata={
            "page": 1,
            "source": "docs.pdf",
        }
    )
    
    print(f"\n📦 Node:")
    print(f"   node_id:  {node.node_id}")         # Auto-generated
    print(f"   text:     {node.text}")
    print(f"   metadata: {node.metadata}")
    
    return node


def demonstrate_relationships():
    """Show how nodes link to each other and to documents."""
    
    print("\n" + "=" * 60)
    print("  Node Relationships")
    print("=" * 60)
    
    # Create a parent document
    doc = Document(
        text="Full document text here...",
        doc_id="doc-001"
    )
    
    # Create child nodes (chunks of the document)
    node_1 = TextNode(
        text="First chunk of text...",
        metadata={"page": 1},
    )
    
    node_2 = TextNode(
        text="Second chunk of text...",
        metadata={"page": 1},
    )
    
    node_3 = TextNode(
        text="Third chunk of text...",
        metadata={"page": 2},
    )
    
    # --- Set relationships ---
    # Link nodes to their source document
    node_1.relationships[NodeRelationship.SOURCE] = RelatedNodeInfo(
        node_id=doc.doc_id
    )
    
    # Link nodes to each other (PREVIOUS / NEXT)
    node_1.relationships[NodeRelationship.NEXT] = RelatedNodeInfo(
        node_id=node_2.node_id
    )
    node_2.relationships[NodeRelationship.PREVIOUS] = RelatedNodeInfo(
        node_id=node_1.node_id
    )
    node_2.relationships[NodeRelationship.NEXT] = RelatedNodeInfo(
        node_id=node_3.node_id
    )
    node_3.relationships[NodeRelationship.PREVIOUS] = RelatedNodeInfo(
        node_id=node_2.node_id
    )
    
    print("\n  Node 1 relationships:")
    for rel_type, rel_info in node_1.relationships.items():
        print(f"    {rel_type.name} → {rel_info.node_id[:20]}...")
    
    print("\n  Node 2 relationships:")
    for rel_type, rel_info in node_2.relationships.items():
        print(f"    {rel_type.name} → {rel_info.node_id[:20]}...")
    
    print("\n💡 Relationships are used by advanced retrievers for")
    print("   hierarchical and parent-child chunk strategies.")


def inspect_document_structure():
    """Show the full internal structure of Document and Node."""
    
    print("\n" + "=" * 60)
    print("  Document vs Node — Comparison")
    print("=" * 60)
    
    comparison = {
        "Document": {
            ".text": "Full source file text",
            ".metadata": "Dict of key-value pairs (filename, page, etc.)",
            ".doc_id": "Unique document identifier",
            ".embedding": "None by default (set after embedding)",
        },
        "TextNode": {
            ".text": "Chunk of text (subset of a Document)",
            ".metadata": "Inherited from parent Document + chunk-specific",
            ".node_id": "Unique node identifier",
            ".embedding": "Vector embedding (set after embedding)",
            ".relationships": "Links to SOURCE doc, PREVIOUS/NEXT nodes",
        }
    }
    
    for obj_type, attrs in comparison.items():
        print(f"\n  📋 {obj_type}:")
        for attr, desc in attrs.items():
            print(f"    {attr:20s} → {desc}")


if __name__ == "__main__":
    create_documents()
    create_nodes()
    demonstrate_relationships()
    inspect_document_structure()
