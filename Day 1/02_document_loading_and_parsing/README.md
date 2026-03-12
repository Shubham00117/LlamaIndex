# Topic 2: Document Loading & Parsing

## Overview
Document loading is the first step in any LlamaIndex pipeline. LlamaIndex provides multiple ways to ingest data — from local files to cloud storage to complex PDFs.

## Key Concepts

### SimpleDirectoryReader (#4)
- Fastest way to load local files (PDF, DOCX, TXT, CSV, HTML, MD)
- Auto-detects file types, creates `Document` objects with `.text` and `.metadata`

### LlamaHub Data Connectors (#5)
- Pre-built connectors for Google Drive, S3, SharePoint, Confluence, OneDrive
- Each is a separate pip install, but all return the same `Document` objects

### LlamaParse (#6)
- Cloud API for parsing complex PDFs with tables, charts, multi-column layouts
- Returns markdown or plain text; requires LlamaCloud API key

### Custom Document Loaders (#7)
- Subclass `BaseReader` to load from proprietary/internal data sources
- Must implement `load_data()` returning a list of `Document` objects

### Documents & Nodes (#8)
- **Document** = full source file (text + metadata + doc_id)
- **Node (TextNode)** = chunk of a Document after splitting (what gets embedded)

### Metadata Extraction (#9)
- Use LLM-powered extractors to auto-generate titles, summaries, keywords
- Run during ingestion (offline), not at query time

## Files
| File | Description |
|------|-------------|
| `01_simple_directory_reader.py` | Loading local files with SimpleDirectoryReader |
| `02_llamahub_connectors.py` | LlamaHub cloud data connectors (S3, Google Drive) |
| `03_llamaparse.py` | Complex PDF parsing with LlamaParse |
| `04_custom_loader.py` | Building custom document loaders |
| `05_documents_and_nodes.py` | Document and TextNode data structures |
| `06_metadata_extraction.py` | LLM-based metadata extraction |
