# Topic 1: Setup & Project Foundation

## Overview
LlamaIndex is a modular framework for building RAG (Retrieval-Augmented Generation) applications. It is split into a lean **core** package (`llama-index-core`) plus optional **integration packages** for LLMs, embeddings, and vector stores.

## Key Concepts

### 1. Installation & Project Structure
- Install only what you need — core + specific integrations
- Recommend a clean project structure: `main.py`, `ingestion.py`, `query.py`, `config.py`, `data/`, `storage/`, `.env`

### 2. Settings Configuration
- `Settings` is a **global singleton** — set it once at startup
- Configure: `Settings.llm`, `Settings.embed_model`, `Settings.chunk_size`, `Settings.chunk_overlap`
- All indexes and pipelines pick up these settings automatically

### 3. Async Programming
- Production LlamaIndex is almost entirely **async**
- Always use `aquery()`, `achat()`, `arun()`, `aload_data()` in APIs
- Use `asyncio.run()` for standalone scripts

## Files
| File | Description |
|------|-------------|
| `01_installation.py` | Package installation and project structure |
| `02_settings_configuration.py` | Global Settings configuration |
| `03_async_basics.py` | Sync vs async patterns, FastAPI integration |
