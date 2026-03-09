"""
Topic 2 — Document Loading & Parsing
Subtopic #4: SimpleDirectoryReader

SimpleDirectoryReader is the fastest way to load local files.
It auto-detects file types: PDF, DOCX, TXT, CSV, HTML, Markdown.

Each loaded file becomes a Document object with:
  - .text     → the file's text content
  - .metadata → dict with filename, page number, etc.

⚠️ Requires: pip install llama-index-core
"""

from llama_index.core import SimpleDirectoryReader


def load_from_directory():
    """Load ALL files from a directory."""
    
    # Point to a folder — it auto-detects and parses all supported files
    documents = SimpleDirectoryReader(
        input_dir="./data"       # Path to folder with your documents
    ).load_data()
    
    print(f"📄 Loaded {len(documents)} document(s)")
    
    # Inspect each document
    for i, doc in enumerate(documents):
        print(f"\n  Document {i + 1}:")
        print(f"    Text preview: {doc.text[:100]}...")
        print(f"    Metadata: {doc.metadata}")
        print(f"    Doc ID: {doc.doc_id}")
    
    return documents


def load_specific_files():
    """Load only specific files by path."""
    
    documents = SimpleDirectoryReader(
        input_files=[
            "./data/report.pdf",
            "./data/notes.txt",
        ]
    ).load_data()
    
    print(f"📄 Loaded {len(documents)} specific file(s)")
    return documents


def load_recursive():
    """Load files from nested subdirectories."""
    
    documents = SimpleDirectoryReader(
        input_dir="./data",
        recursive=True    # Descend into all subdirectories
    ).load_data()
    
    print(f"📄 Loaded {len(documents)} document(s) from nested dirs")
    return documents


def load_with_filters():
    """Load only certain file types."""
    
    documents = SimpleDirectoryReader(
        input_dir="./data",
        required_exts=[".pdf", ".txt"],  # Only load PDF and TXT files
        recursive=True,
    ).load_data()
    
    print(f"📄 Loaded {len(documents)} filtered document(s)")
    return documents


def load_with_custom_metadata():
    """Add custom metadata to all loaded documents."""
    
    # You can attach extra metadata to every loaded document
    documents = SimpleDirectoryReader(
        input_dir="./data"
    ).load_data()
    
    # Add custom metadata after loading
    for doc in documents:
        doc.metadata["project"] = "my_rag_app"
        doc.metadata["version"] = "1.0"
    
    print(f"📄 Loaded {len(documents)} document(s) with custom metadata")
    if documents:
        print(f"   Example metadata: {documents[0].metadata}")
    
    return documents


if __name__ == "__main__":
    import os
    
    # Create a sample data directory for testing
    os.makedirs("./data", exist_ok=True)
    
    # Create a sample text file
    sample_file = "./data/sample.txt"
    if not os.path.exists(sample_file):
        with open(sample_file, "w") as f:
            f.write("LlamaIndex is a framework for building RAG applications.\n")
            f.write("It connects LLMs with your data sources.\n")
            f.write("RAG stands for Retrieval Augmented Generation.\n")
    
    # Run the examples
    print("=" * 60)
    print("  SimpleDirectoryReader — Loading Local Files")
    print("=" * 60)
    
    docs = load_from_directory()
    
    print("\n" + "=" * 60)
    print("  With Custom Metadata")
    print("=" * 60)
    
    load_with_custom_metadata()
