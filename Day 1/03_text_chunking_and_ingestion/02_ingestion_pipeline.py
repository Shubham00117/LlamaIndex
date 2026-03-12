"""
Topic 3 — Text Chunking & Ingestion
Subtopic #11: Ingestion Pipeline

IngestionPipeline chains transformations (splitting, metadata extraction,
embedding) into a single reusable pipeline.

Key production feature: INCREMENTAL INDEXING
  - Caches processed nodes via a docstore
  - Re-running never re-embeds already-processed data
  - Only new/changed documents are processed

⚠️ Requires: pip install llama-index-core llama-index-embeddings-openai
"""

import asyncio
from llama_index.core.schema import Document


async def basic_pipeline():
    """Create a basic ingestion pipeline."""
    
    from llama_index.core.ingestion import IngestionPipeline
    from llama_index.core.node_parser import SentenceSplitter
    from llama_index.embeddings.openai import OpenAIEmbedding
    
    documents = [
        Document(text="LlamaIndex provides tools for building RAG applications."),
        Document(text="Vector stores like Pinecone and Qdrant store embeddings."),
    ]
    
    # Pipeline: split → embed
    pipeline = IngestionPipeline(
        transformations=[
            SentenceSplitter(chunk_size=512, chunk_overlap=50),
            OpenAIEmbedding(),   # Embeds each node
        ]
    )
    
    # Run pipeline (async)
    nodes = await pipeline.arun(documents=documents)
    
    print(f"✅ Processed {len(nodes)} nodes")
    for node in nodes:
        print(f"   Has embedding: {node.embedding is not None}")
    
    return nodes


async def incremental_pipeline():
    """Pipeline with incremental indexing — avoids re-embedding."""
    
    from llama_index.core.ingestion import IngestionPipeline
    from llama_index.core.node_parser import SentenceSplitter
    from llama_index.core.storage.docstore import SimpleDocumentStore
    from llama_index.embeddings.openai import OpenAIEmbedding
    
    # The docstore tracks which documents have been processed
    pipeline = IngestionPipeline(
        transformations=[
            SentenceSplitter(),
            OpenAIEmbedding(),
        ],
        docstore=SimpleDocumentStore(),   # Enables incremental processing
    )
    
    # First run — processes all documents
    docs_v1 = [
        Document(text="Original document content.", doc_id="doc-001"),
        Document(text="Another document.", doc_id="doc-002"),
    ]
    nodes_v1 = await pipeline.arun(documents=docs_v1)
    print(f"First run: {len(nodes_v1)} nodes processed")
    
    # Second run — only new/changed docs are processed
    docs_v2 = [
        Document(text="Original document content.", doc_id="doc-001"),  # Unchanged
        Document(text="Updated content here!", doc_id="doc-002"),       # Changed
        Document(text="Brand new document.", doc_id="doc-003"),         # New
    ]
    nodes_v2 = await pipeline.arun(documents=docs_v2)
    print(f"Second run: {len(nodes_v2)} nodes processed (only changed/new)")
    
    return nodes_v2


def show_pipeline_concepts():
    """Explain the ingestion pipeline concepts."""
    
    print("=" * 60)
    print("  Ingestion Pipeline Concepts")
    print("=" * 60)
    
    print("\n  📋 Pipeline Flow:")
    print("     Documents → [Transform 1] → [Transform 2] → ... → Nodes")
    
    print("\n  📋 Common Transformations:")
    print("     1. SentenceSplitter   → Split docs into chunks")
    print("     2. TitleExtractor     → Extract titles via LLM")
    print("     3. OpenAIEmbedding    → Generate embeddings")
    
    print("\n  ⚡ Incremental Indexing:")
    print("     • Add a docstore to the pipeline")
    print("     • Pipeline tracks processed documents by hash")
    print("     • Re-runs only process new/changed documents")
    print("     • Saves money and time in production!")


if __name__ == "__main__":
    show_pipeline_concepts()
    
    print("\n💡 To run the async examples:")
    print("   asyncio.run(basic_pipeline())")
    print("   asyncio.run(incremental_pipeline())")
    
    # Uncomment to run (requires OPENAI_API_KEY):
    # asyncio.run(basic_pipeline())
