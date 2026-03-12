# Topic 4: Indexing

## Overview
Indexing is the process of organizing your chunked, embedded data for efficient retrieval. The `VectorStoreIndex` is the core index used in nearly all RAG applications.

## Key Concepts
- **VectorStoreIndex** (#14): Core index — embeds nodes and stores in vector store
- **Document Management** (#15): Add, delete, refresh documents without rebuilding
- **Metadata Filtering** (#16): Tag nodes with metadata, filter at query time (multi-tenant)
- **Property Graph Index** (#17): Knowledge graph RAG for multi-hop reasoning
- **Persistent Storage** (#18): Save/load index to disk or external vector DB
