"""
Topic 8 — Query Engine & Retrieval
Subtopic #43: Metadata Filtering in Queries

Filter retrieved nodes by metadata at query time.
Essential for multi-tenant apps and scoped searches.

⚠️ Requires: pip install llama-index-core
"""

from llama_index.core.vector_stores import MetadataFilter, MetadataFilters, FilterOperator


def metadata_query_examples():
    """Show metadata filtering patterns."""
    
    code = '''
from llama_index.core.vector_stores import (
    MetadataFilter, MetadataFilters, FilterOperator
)

# Filter by exact match
filters = MetadataFilters(filters=[
    MetadataFilter(key="department", value="finance"),
])

# Filter with operators
filters = MetadataFilters(filters=[
    MetadataFilter(key="year", value=2024, operator=FilterOperator.GTE),
    MetadataFilter(key="department", value="engineering"),
])

# Apply to query engine
query_engine = index.as_query_engine(
    filters=filters,
    similarity_top_k=5,
)

response = await query_engine.aquery("What were the results?")
'''
    
    print("=" * 60)
    print("  Metadata Filtering in Queries")
    print("=" * 60)
    print(code)
    
    print("📋 Filter Operators:")
    print("  EQ  → Equal")
    print("  NE  → Not equal")
    print("  GT  → Greater than")
    print("  GTE → Greater than or equal")
    print("  LT  → Less than")
    print("  LTE → Less than or equal")
    print("  IN  → In a list of values")


if __name__ == "__main__":
    metadata_query_examples()
