"""
Topic 2 — Document Loading & Parsing
Subtopic #7: Custom Document Loaders

When no pre-built connector exists for your data source
(internal databases, proprietary APIs, custom formats),
build your own by subclassing BaseReader.

Pattern:
  1. Subclass BaseReader
  2. Implement load_data() method
  3. Return a list of Document objects

⚠️ Requires: pip install llama-index-core
"""

from llama_index.core.readers.base import BaseReader
from llama_index.core.schema import Document
from typing import List


# ─────────────────────────────────────────────────────────────
# Example 1: Custom API Data Loader
# ─────────────────────────────────────────────────────────────

class MyApiReader(BaseReader):
    """
    Custom reader that fetches data from an internal REST API.
    Replace the API call with your actual data source.
    """
    
    def __init__(self, api_url: str, api_key: str = None):
        """Initialize with API connection details."""
        self.api_url = api_url
        self.api_key = api_key
    
    def load_data(self, **kwargs) -> List[Document]:
        """
        Fetch data from the API and return Document objects.
        This is the only method you MUST implement.
        """
        # Simulating an API call — replace with actual requests
        raw_data = [
            {"id": "1", "content": "First article content", "author": "Alice", "date": "2024-01-15"},
            {"id": "2", "content": "Second article content", "author": "Bob", "date": "2024-02-20"},
            {"id": "3", "content": "Third article content", "author": "Charlie", "date": "2024-03-10"},
        ]
        
        # Convert each API response item to a Document
        documents = [
            Document(
                text=item["content"],          # The actual text content
                metadata={
                    "source": f"api/{item['id']}",   # Track where it came from
                    "author": item["author"],
                    "date": item["date"],
                }
            )
            for item in raw_data
        ]
        
        return documents


# ─────────────────────────────────────────────────────────────
# Example 2: Custom Database Loader
# ─────────────────────────────────────────────────────────────

class DatabaseReader(BaseReader):
    """
    Custom reader that loads documents from a SQL database.
    """
    
    def __init__(self, connection_string: str):
        """Initialize with database connection string."""
        self.connection_string = connection_string
    
    def load_data(self, query: str = None, **kwargs) -> List[Document]:
        """
        Execute a SQL query and return results as Documents.
        """
        # Simulating database results
        # In production: use sqlalchemy or similar to execute the query
        rows = [
            {"id": 1, "title": "Product Guide", "body": "How to use our product...", "category": "docs"},
            {"id": 2, "title": "FAQ", "body": "Common questions and answers...", "category": "support"},
        ]
        
        documents = []
        for row in rows:
            doc = Document(
                text=f"{row['title']}\n\n{row['body']}",
                metadata={
                    "source": f"db/row/{row['id']}",
                    "category": row["category"],
                    "title": row["title"],
                }
            )
            documents.append(doc)
        
        return documents


# ─────────────────────────────────────────────────────────────
# Example 3: Custom CSV/Excel Loader with Processing
# ─────────────────────────────────────────────────────────────

class ProcessedCsvReader(BaseReader):
    """
    Custom reader that loads CSV files with extra processing
    (e.g., combining columns, filtering rows, cleaning data).
    """
    
    def __init__(self, combine_columns: list = None):
        """Initialize with processing options."""
        self.combine_columns = combine_columns or []
    
    def load_data(self, file_path: str = None, **kwargs) -> List[Document]:
        """Load and process a CSV file."""
        import csv
        
        documents = []
        
        # Read CSV
        with open(file_path, "r") as f:
            reader = csv.DictReader(f)
            for row_num, row in enumerate(reader):
                # Combine specified columns into text
                if self.combine_columns:
                    text_parts = [f"{col}: {row.get(col, '')}" for col in self.combine_columns]
                    text = "\n".join(text_parts)
                else:
                    text = "\n".join(f"{k}: {v}" for k, v in row.items())
                
                doc = Document(
                    text=text,
                    metadata={
                        "source": file_path,
                        "row_number": row_num,
                        **{k: v for k, v in row.items() if k not in self.combine_columns}
                    }
                )
                documents.append(doc)
        
        return documents


if __name__ == "__main__":
    print("=" * 60)
    print("  Custom Document Loaders")
    print("=" * 60)
    
    # Test the API reader
    print("\n📡 Custom API Reader:")
    api_reader = MyApiReader(api_url="https://api.example.com/articles")
    api_docs = api_reader.load_data()
    
    for doc in api_docs:
        print(f"  Source: {doc.metadata['source']}, Author: {doc.metadata['author']}")
        print(f"  Text: {doc.text[:50]}...")
    
    # Test the database reader
    print("\n🗄️  Custom Database Reader:")
    db_reader = DatabaseReader(connection_string="sqlite:///my_database.db")
    db_docs = db_reader.load_data()
    
    for doc in db_docs:
        print(f"  Category: {doc.metadata['category']}, Title: {doc.metadata['title']}")
    
    print("\n💡 Your custom readers return standard Document objects,")
    print("   so they work with ALL LlamaIndex indexes and pipelines!")
