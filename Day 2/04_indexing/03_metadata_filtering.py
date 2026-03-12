"""
Topic 4 — Indexing
Subtopic #16: Metadata Filtering During Indexing

Tag nodes with metadata at ingestion time, then filter by it at query time.
This is how you build:
  - Multi-tenant systems (user-level data isolation)
  - Date-range queries
  - Department-specific knowledge bases

⚠️ Requires: pip install llama-index-core
"""

from llama_index.core.schema import Document
from llama_index.core.vector_stores import (
    MetadataFilter,
    MetadataFilters,
    FilterOperator,
)


def set_metadata_on_documents():
    """Create documents with structured metadata for filtering."""
    
    documents = [
        Document(
            text="Q3 financial results show 15% revenue growth...",
            metadata={
                "department": "finance",
                "year": 2024,
                "quarter": "Q3",
                "user_id": "tenant_42",
            }
        ),
        Document(
            text="New product launch scheduled for October...",
            metadata={
                "department": "marketing",
                "year": 2024,
                "quarter": "Q4",
                "user_id": "tenant_42",
            }
        ),
        Document(
            text="Engineering team completed migration to microservices...",
            metadata={
                "department": "engineering",
                "year": 2024,
                "quarter": "Q3",
                "user_id": "tenant_99",
            }
        ),
    ]
    
    print("📄 Documents with metadata:")
    for doc in documents:
        print(f"  dept={doc.metadata['department']}, "
              f"year={doc.metadata['year']}, "
              f"tenant={doc.metadata['user_id']}")
    
    return documents


def filter_at_query_time():
    """Show how to build metadata filters for queries."""
    
    print("\n" + "=" * 60)
    print("  Metadata Filtering at Query Time")
    print("=" * 60)
    
    # Filter by department
    dept_filter = MetadataFilters(filters=[
        MetadataFilter(key="department", value="finance"),
    ])
    
    # Filter by department AND year
    combined_filter = MetadataFilters(filters=[
        MetadataFilter(key="department", value="finance"),
        MetadataFilter(key="year", value=2024, operator=FilterOperator.EQ),
    ])
    
    # Multi-tenant filter (critical for data isolation)
    tenant_filter = MetadataFilters(filters=[
        MetadataFilter(key="user_id", value="tenant_42"),
    ])
    
    print("\n  Example usage:")
    print("  query_engine = index.as_query_engine(filters=dept_filter)")
    print("  response = await query_engine.aquery('Q3 results?')")
    
    print("\n  🔒 Multi-tenant pattern:")
    print("  Always filter by user_id at query time.")
    print("  This prevents users from retrieving each other's data.")
    
    return combined_filter


if __name__ == "__main__":
    set_metadata_on_documents()
    filter_at_query_time()
