"""
Topic 3 — Text Chunking & Ingestion
Subtopic #12: Transformations in Ingestion Pipeline

Any step in the pipeline is a Transformation. They are composable
and run in sequence. You can mix splitters, metadata extractors,
and embedding models freely.

⚠️ LLM-based transformations (TitleExtractor, QuestionsAnsweredExtractor)
   cost tokens. Use them only when retrieval quality justifies the cost.

⚠️ Requires: pip install llama-index-core llama-index-embeddings-openai
"""


def show_full_production_pipeline():
    """Show a full production ingestion pipeline with all steps."""
    
    pipeline_code = '''
from llama_index.core.extractors import (
    TitleExtractor,
    QuestionsAnsweredExtractor,
)
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.openai import OpenAIEmbedding

pipeline = IngestionPipeline(
    transformations=[
        # Step 1 — Split into chunks
        SentenceSplitter(chunk_size=512, chunk_overlap=50),

        # Step 2 — Extract metadata via LLM
        TitleExtractor(),
        QuestionsAnsweredExtractor(questions=3),

        # Step 3 — Generate embeddings
        OpenAIEmbedding(model="text-embedding-3-small"),
    ]
)

# Run the pipeline
nodes = await pipeline.arun(documents=documents)
'''
    
    print("=" * 60)
    print("  Full Production Pipeline")
    print("=" * 60)
    print(pipeline_code)
    
    print("📋 Pipeline Steps Explained:")
    print("  1. SentenceSplitter → Splits documents into manageable chunks")
    print("  2. TitleExtractor   → Uses LLM to extract document title")
    print("  3. QuestionsAnsweredExtractor → Generates hypothetical questions")
    print("  4. OpenAIEmbedding  → Converts each chunk to a vector")
    
    print("\n⚠️  Cost Warning:")
    print("  LLM-based transformations call your LLM per node.")
    print("  Use them only when retrieval quality justifies the cost.")
    
    print("\n✅ Properties of Transformations:")
    print("  • Composable — mix and match any transformations")
    print("  • Sequential — run in the order you list them")
    print("  • Cached — results are cached for incremental processing")


if __name__ == "__main__":
    show_full_production_pipeline()
