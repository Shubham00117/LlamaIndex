"""
Topic 4 — Indexing
Subtopic #15: Document Management — Add, Delete, Refresh

Production indexes need to stay up to date. LlamaIndex provides
methods to insert, delete, and refresh documents without rebuilding.

Methods:
  index.insert(doc)          → Add a new document
  index.delete_ref_doc(id)   → Remove a document by ID
  index.refresh_ref_docs()   → Re-index only changed documents

⚠️ Requires: pip install llama-index-core
"""

from llama_index.core.schema import Document


def document_management_patterns():
    """Show all document management operations."""
    
    print("=" * 60)
    print("  Document Management Patterns")
    print("=" * 60)
    
    insert_code = '''
# --- INSERT new documents ---
from llama_index.core import Document

new_doc = Document(text="New content here...")

# Insert into existing index
index.insert(new_doc)
'''
    
    delete_code = '''
# --- DELETE documents by ID ---
# Delete a document and all its nodes
index.delete_ref_doc(
    "doc_id_here",
    delete_from_docstore=True  # Also remove from docstore
)
'''
    
    refresh_code = '''
# --- REFRESH — update changed documents ---
# Only re-indexes documents whose content has changed
refreshed_docs = index.refresh_ref_docs(
    updated_documents,
    update_kwargs={
        "delete_kwargs": {"delete_from_docstore": True}
    }
)
'''
    
    print("\n📥 INSERT:")
    print(insert_code)
    print("📤 DELETE:")
    print(delete_code)
    print("🔄 REFRESH:")
    print(refresh_code)
    
    print("📋 Method Reference:")
    print("  insert()          → Add a new document to the index")
    print("  delete_ref_doc()  → Remove a document and its nodes by doc ID")
    print("  refresh_ref_docs()→ Re-index documents — only updates changed ones")


if __name__ == "__main__":
    document_management_patterns()
