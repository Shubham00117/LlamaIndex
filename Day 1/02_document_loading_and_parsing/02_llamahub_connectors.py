"""
Topic 2 — Document Loading & Parsing
Subtopic #5: LlamaHub Data Connectors

LlamaHub provides pre-built connectors for external data sources.
Each connector is a separate pip package but returns the same
Document objects — your indexing code stays the same.

Common connectors:
  - Google Drive:  llama-index-readers-google
  - S3 / AWS:     llama-index-readers-s3
  - SharePoint:   llama-index-readers-microsoft-sharepoint
  - Confluence:   llama-index-readers-confluence
  - OneDrive:     llama-index-readers-microsoft-onedrive

⚠️ Each connector requires its own pip install.
"""


def load_from_s3():
    """
    Load documents from an AWS S3 bucket.
    pip install llama-index-readers-s3
    """
    from llama_index.readers.s3 import S3Reader
    
    reader = S3Reader(
        bucket="my-company-docs",          # S3 bucket name
        prefix="contracts/",               # Only load files under this prefix
        aws_access_id="YOUR_ACCESS_KEY",   # AWS credentials
        aws_access_secret="YOUR_SECRET",
    )
    
    # Returns standard Document objects
    documents = reader.load_data()
    
    print(f"📄 Loaded {len(documents)} document(s) from S3")
    return documents


def load_from_google_drive():
    """
    Load documents from Google Drive.
    pip install llama-index-readers-google
    """
    from llama_index.readers.google import GoogleDriveReader
    
    reader = GoogleDriveReader(
        # You need to set up Google API credentials first
        # See: https://developers.google.com/drive/api/quickstart/python
    )
    
    # Load from a specific folder by ID
    documents = reader.load_data(folder_id="YOUR_FOLDER_ID")
    
    print(f"📄 Loaded {len(documents)} document(s) from Google Drive")
    return documents


def load_from_confluence():
    """
    Load pages from Atlassian Confluence wiki.
    pip install llama-index-readers-confluence
    """
    from llama_index.readers.confluence import ConfluenceReader
    
    reader = ConfluenceReader(
        base_url="https://your-domain.atlassian.net/wiki",
    )
    
    # Load pages from a specific space
    documents = reader.load_data(
        space_key="ENG",        # Confluence space key
        include_attachments=True,
    )
    
    print(f"📄 Loaded {len(documents)} page(s) from Confluence")
    return documents


def show_connector_reference():
    """Display a reference table of available data connectors."""
    
    print("=" * 60)
    print("  LlamaHub Data Connectors Reference")
    print("=" * 60)
    
    connectors = {
        "Google Drive": "llama-index-readers-google",
        "AWS S3": "llama-index-readers-s3",
        "SharePoint": "llama-index-readers-microsoft-sharepoint",
        "Confluence": "llama-index-readers-confluence",
        "OneDrive": "llama-index-readers-microsoft-onedrive",
        "Notion": "llama-index-readers-notion",
        "Slack": "llama-index-readers-slack",
        "GitHub": "llama-index-readers-github",
        "Web Pages": "llama-index-readers-web",
        "Database (SQL)": "llama-index-readers-database",
    }
    
    for source, package in connectors.items():
        print(f"\n  📡 {source}")
        print(f"     pip install {package}")
    
    print("\n💡 All connectors return the same Document objects.")
    print("   Your indexing code stays the same regardless of the source!")


if __name__ == "__main__":
    show_connector_reference()
    
    print("\n⚠️  To run the actual connectors, install the specific package")
    print("   and configure your credentials (API keys, tokens, etc.)")
