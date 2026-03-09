"""
LlamaIndex Example: LlamaHub Data Connectors
--------------------------------------------
LlamaHub (llamahub.ai) is a community-driven repository of data connectors. 
These connectors allow you to ingest data from hundreds of external platforms 
like Google Drive, S3, Notion, Slack, and GitHub.

Key Benefits:
  - Unified Interface: Every connector returns standard LlamaIndex `Document` objects.
  - Decoupled Code: Your indexing and query logic remains unchanged regardless of the source.
  - Extensibility: You can easily switch between data sources with minimal code changes.

Note: Each connector usually requires its own specific pip package installation.

Documentation: https://llamahub.ai/
"""


def load_from_s3():
    """
    Example: Loading documents from an AWS S3 bucket.
    Requires: pip install llama-index-readers-s3
    
    This reader is ideal for companies storing massive document datasets in the cloud.
    """
    from llama_index.readers.s3 import S3Reader
    
    # Configuration for the S3 Reader
    reader = S3Reader(
        bucket="my-company-documents",      # Name of your S3 bucket
        prefix="contracts/",               # Optional: filter by sub-folder/prefix
        aws_access_id="YOUR_ACCESS_KEY",   # Use environment variables in production!
        aws_access_secret="YOUR_SECRET",
    )
    
    # Executes retrieval and returns standard Document objects
    documents = reader.load_data()
    
    print(f"📄 Successfully retrieved {len(documents)} document(s) from AWS S3.")
    return documents


def load_from_google_drive():
    """
    Example: Loading documents from Google Drive.
    Requires: pip install llama-index-readers-google
    
    Note: Requires setting up a Google Cloud Project and obtaining 
    `credentials.json` from the Google Developer Console.
    """
    from llama_index.readers.google import GoogleDriveReader
    
    reader = GoogleDriveReader()
    
    # You can load from a specific folder ID or individual file IDs
    documents = reader.load_data(folder_id="YOUR_GOOGLE_DRIVE_FOLDER_ID")
    
    print(f"📄 Successfully retrieved {len(documents)} document(s) from Google Drive.")
    return documents


def load_from_confluence():
    """
    Example: Loading wiki pages from Atlassian Confluence.
    Requires: pip install llama-index-readers-confluence
    
    Useful for building RAG systems on top of internal company wikis.
    """
    from llama_index.readers.confluence import ConfluenceReader
    
    reader = ConfluenceReader(
        base_url="https://your-domain.atlassian.net/wiki",
    )
    
    # Load pages from a specific Confluence space
    documents = reader.load_data(
        space_key="ENGINEERING",  # Confluence Space Key
        include_attachments=True, # Also parse PDFs/images attached to pages
    )
    
    print(f"📄 Successfully retrieved {len(documents)} page(s) from Confluence.")
    return documents


def show_connector_reference():
    """Displays a reference table of popular data connectors and their packages."""
    
    print("=" * 60)
    print("  LlamaHub Data Connectors Reference Guide")
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
        print(f"     Installation: pip install {package}")
    
    print("\n💡 Core Insight: All connectors normalize data into Document objects.")
    print("   This means your RAG pipeline doesn't care WHERE the data comes from!")


if __name__ == "__main__":
    # Print the reference guide for the user
    show_connector_reference()
    
    print("\n⚠️  DEVELOPER NOTE:")
    print("   To execute these readers, you must install the associated package")
    print("   and configure the necessary API credentials/tokens.")
