"""
LlamaIndex Example: SimpleDirectoryReader
-----------------------------------------
SimpleDirectoryReader is the fastest and easiest way to ingest local data into 
LlamaIndex. It automatically detects and parses a wide variety of file formats 
including PDF, DOCX, TXT, CSV, HTML, and Markdown.

Core Concept:
  Each loaded file is converted into one or more `Document` objects.
  A Document contains:
    - .text: The raw text extracted from the file.
    - .metadata: A dictionary containing source information (filename, path, etc.).
    - .doc_id: A unique identifier for the document.

Requirements:
  pip install llama-index-core
"""

from llama_index.core import SimpleDirectoryReader


def load_from_directory():
    """
    Demonstrates loading ALL supported files from a single directory.
    
    LlamaIndex will automatically attempt to parse every file it finds 
    using built-in readers.
    
    Returns:
        List[Document]: A list of LlamaIndex Document objects.
    """
    
    # Point to the data folder - auto-discovery of file types
    documents = SimpleDirectoryReader(
        input_dir="./data"  # Path to your local document repository
    ).load_data()
    
    print(f"📄 Successfully loaded {len(documents)} document(s)")
    
    # Inspection of the loaded Document objects
    for i, doc in enumerate(documents):
        print(f"\n[Document {i + 1}]")
        print(f"  Preview (100 chars): {doc.text[:100].strip()}...")
        print(f"  Metadata: {doc.metadata}")
        print(f"  Unique Doc ID: {doc.doc_id}")
    
    return documents


def load_specific_files():
    """
    Demonstrates loading a targeted list of files rather than an entire directory.
    Use this when you want precise control over which documents enter your index.
    """
    
    documents = SimpleDirectoryReader(
        input_files=[
            "./data/sample.txt",
            # "./data/report.pdf",  # Add paths to your specific files here
        ]
    ).load_data()
    
    print(f"📄 Loaded {len(documents)} specific files.")
    return documents


def load_recursive():
    """
    Demonstrates recursive loading from nested subdirectories.
    Perfect for large, organized documentation sets.
    """
    
    documents = SimpleDirectoryReader(
        input_dir="./data",
        recursive=True  # Enables traversal into all sub-folders
    ).load_data()
    
    print(f"📄 Recursively loaded {len(documents)} document(s) from directory tree.")
    return documents


def load_with_filters():
    """
    Demonstrates filtering for specific file extensions.
    Prevents the ingestion of unwanted file types (e.g., system files, images).
    """
    
    documents = SimpleDirectoryReader(
        input_dir="./data",
        required_exts=[".pdf", ".txt"],  # Strict whitelist of extensions
        recursive=True,
    ).load_data()
    
    print(f"📄 Filtered loading complete: {len(documents)} documents found (PDF/TXT only).")
    return documents


def load_with_custom_metadata():
    """
    Demonstrates how to enrich Document objects with custom metadata 
    immediately after loading. Metadata can be used later for filtering 
    replies or adding context to the LLM.
    """
    
    documents = SimpleDirectoryReader(input_dir="./data").load_data()
    
    # Enriching each document with application-specific context
    for doc in documents:
        doc.metadata["project_name"] = "Knowledge_Base_Alpha"
        doc.metadata["ingestion_source"] = "local_filesystem"
        doc.metadata["classification"] = "internal_use_only"
    
    print(f"📄 Enhanced {len(documents)} documents with custom metadata fields.")
    if documents:
        print(f"   Sample Metadata: {documents[0].metadata}")
    
    return documents


if __name__ == "__main__":
    import os
    
    # --- SETUP: Ensure a data directory exists for the demonstration ---
    os.makedirs("./data", exist_ok=True)
    
    # Create a dummy file if none exists
    sample_file = "./data/sample.txt"
    if not os.path.exists(sample_file):
        with open(sample_file, "w") as f:
            f.write("LlamaIndex is the leading framework for building RAG applications.\n")
            f.write("It bridges the gap between your custom data and Large Language Models.\n")
            f.write("SimpleDirectoryReader is the entry point for most RAG pipelines.\n")
    
    # --- EXECUTION: Run the examples ---
    print("=" * 60)
    print("  LlamaIndex - SimpleDirectoryReader Implementation Guide")
    print("=" * 60)
    
    load_from_directory()
    
    print("\n" + "-" * 60)
    print("  Adding Custom Metadata at Ingestion")
    print("-" * 60)
    
    load_with_custom_metadata()
