"""
Topic 2 — Document Loading & Parsing
Subtopic #9: Metadata Extraction

Automatically extract structured metadata from documents using LLMs.
This metadata improves retrieval quality significantly.

Available extractors:
  - TitleExtractor          → Extracts document title using LLM
  - SummaryExtractor        → Generates a summary for each node
  - QuestionsAnsweredExtractor → Generates hypothetical questions the node answers
  - KeywordExtractor        → Extracts key terms for keyword-based filtering

⚠️ Metadata extraction calls your LLM per node — adds cost & latency.
   Use it during INGESTION (offline), NOT at query time.

⚠️ Requires: pip install llama-index-core llama-index-llms-openai
"""

import asyncio


async def basic_metadata_extraction():
    """Extract titles and questions from documents using LLM."""
    
    from llama_index.core.extractors import (
        TitleExtractor,
        QuestionsAnsweredExtractor,
    )
    from llama_index.core.ingestion import IngestionPipeline
    from llama_index.core.node_parser import SentenceSplitter
    from llama_index.core.schema import Document
    
    # Create sample documents
    documents = [
        Document(
            text="LlamaIndex is a data framework for LLM applications. "
                 "It provides tools for ingesting, structuring, and accessing "
                 "private or domain-specific data. The main pattern is RAG — "
                 "Retrieval Augmented Generation — where relevant context is "
                 "retrieved from a knowledge base and fed to an LLM."
        ),
    ]
    
    # Build an ingestion pipeline with metadata extractors
    pipeline = IngestionPipeline(
        transformations=[
            # Step 1: Split into chunks
            SentenceSplitter(chunk_size=256, chunk_overlap=30),
            
            # Step 2: Extract title using LLM
            TitleExtractor(),
            
            # Step 3: Generate hypothetical questions each node answers
            QuestionsAnsweredExtractor(questions=3),
        ]
    )
    
    # Run the pipeline (async)
    nodes = await pipeline.arun(documents=documents)
    
    print("📄 Extracted metadata for each node:")
    for i, node in enumerate(nodes):
        print(f"\n  Node {i + 1}:")
        print(f"    Text: {node.text[:80]}...")
        print(f"    Metadata keys: {list(node.metadata.keys())}")
        if "document_title" in node.metadata:
            print(f"    Title: {node.metadata['document_title']}")
        if "questions_this_excerpt_can_answer" in node.metadata:
            print(f"    Questions: {node.metadata['questions_this_excerpt_can_answer']}")
    
    return nodes


async def full_extraction_pipeline():
    """Complete pipeline with all common extractors."""
    
    from llama_index.core.extractors import (
        TitleExtractor,
        SummaryExtractor,
        QuestionsAnsweredExtractor,
        KeywordExtractor,
    )
    from llama_index.core.ingestion import IngestionPipeline
    from llama_index.core.node_parser import SentenceSplitter
    
    # Full production pipeline
    pipeline = IngestionPipeline(
        transformations=[
            SentenceSplitter(chunk_size=512, chunk_overlap=50),
            TitleExtractor(),
            SummaryExtractor(summaries=["self"]),  # Summary of each chunk
            QuestionsAnsweredExtractor(questions=3),
            KeywordExtractor(keywords=5),
        ]
    )
    
    print("📋 Full Extraction Pipeline:")
    print("   1. SentenceSplitter  → chunk documents")
    print("   2. TitleExtractor    → extract document title")
    print("   3. SummaryExtractor  → generate chunk summaries")
    print("   4. QuestionsAnswered → generate hypothetical questions")
    print("   5. KeywordExtractor  → extract key terms")
    
    return pipeline


def show_extractor_reference():
    """Display reference table of metadata extractors."""
    
    print("=" * 60)
    print("  Metadata Extractors Reference")
    print("=" * 60)
    
    extractors = {
        "TitleExtractor": "Extracts document title using LLM",
        "SummaryExtractor": "Generates a summary for each node/section",
        "QuestionsAnsweredExtractor": "Generates hypothetical questions the node answers — great for HyDE",
        "KeywordExtractor": "Extracts key terms for keyword-based filtering",
    }
    
    for name, description in extractors.items():
        print(f"\n  🔹 {name}")
        print(f"     {description}")
    
    print("\n⚠️  Cost Warning:")
    print("   LLM-based extractors call your LLM per node.")
    print("   100 nodes × 4 extractors = 400 LLM calls.")
    print("   Use during ingestion (offline), not at query time.")


if __name__ == "__main__":
    show_extractor_reference()
    
    print("\n💡 Run with: asyncio.run(basic_metadata_extraction())")
    print("   to see the extractors in action.")
    
    # Uncomment to run (requires OPENAI_API_KEY):
    # asyncio.run(basic_metadata_extraction())
