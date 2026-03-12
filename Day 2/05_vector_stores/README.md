# Topic 5: Vector Stores (Production DBs)

## Overview
Vector stores hold embeddings for fast similarity search. The setup pattern is always the same: **create vector_store → wrap in StorageContext → pass to VectorStoreIndex**.

## Stores Covered
| Store | Type | Best For |
|-------|------|----------|
| Pinecone | Cloud | Fastest to production, zero infra |
| Qdrant | OSS/Cloud | Rich filtering, self-hosted control |
| ChromaDB | Local | Local dev, prototyping |
| Weaviate | Hybrid | Built-in BM25 + vector search |
| Milvus | OSS | Billion-scale vectors |
| MongoDB Atlas | Cloud | If you already use MongoDB |
| PGVector | SQL+Vec | Postgres users, SQL + vector |
| Redis | Cache+Vec | Ultra-low latency (<5ms) |
