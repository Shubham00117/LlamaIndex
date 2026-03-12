"""
Topic 2 — Document Loading & Parsing
Subtopic #6: LlamaParse — Complex PDF Parsing

Standard PDF readers fail on:
  - Tables with complex layouts
  - Multi-column documents
  - Charts and embedded images
  - Financial / legal documents

LlamaParse is a cloud API that extracts these accurately.
It returns results as markdown (preserves structure) or plain text.

⚠️ Requires: pip install llama-parse
⚠️ Requires: LLAMA_CLOUD_API_KEY environment variable
"""

import asyncio
import os


async def parse_complex_pdf():
    """
    Parse a complex PDF using LlamaParse.
    Best for: tables, charts, multi-column PDFs.
    """
    from llama_parse import LlamaParse
    
    parser = LlamaParse(
        api_key=os.environ["LLAMA_CLOUD_API_KEY"],
        result_type="markdown",   # "markdown" or "text"
        verbose=True,             # Show progress
    )
    
    # Parse a PDF file (async)
    documents = await parser.aload_data("./data/report.pdf")
    
    print(f"📄 Parsed {len(documents)} document(s)")
    for doc in documents:
        print(f"   Preview: {doc.text[:200]}...")
    
    return documents


async def parse_with_options():
    """
    LlamaParse with advanced options for better extraction.
    """
    from llama_parse import LlamaParse
    
    parser = LlamaParse(
        api_key=os.environ["LLAMA_CLOUD_API_KEY"],
        result_type="markdown",       # Markdown preserves table structure
        verbose=True,
        language="en",                # Document language
        num_workers=4,                # Parallel processing for multiple files
    )
    
    # Parse multiple files at once
    documents = await parser.aload_data([
        "./data/financial_report.pdf",
        "./data/legal_contract.pdf",
    ])
    
    return documents


def use_llamaparse_with_directory_reader():
    """
    Use LlamaParse as the PDF parser inside SimpleDirectoryReader.
    This lets you use LlamaParse for PDFs while keeping SimpleDirectoryReader
    for everything else.
    """
    from llama_index.core import SimpleDirectoryReader
    from llama_parse import LlamaParse
    
    # Create a parser for PDFs
    parser = LlamaParse(
        api_key=os.environ["LLAMA_CLOUD_API_KEY"],
        result_type="markdown",
    )
    
    # Map file extensions to custom parsers
    file_extractor = {".pdf": parser}
    
    # SimpleDirectoryReader will use LlamaParse for PDFs,
    # default parsers for everything else
    documents = SimpleDirectoryReader(
        input_dir="./data",
        file_extractor=file_extractor,  # Custom parser map
    ).load_data()
    
    return documents


def show_result_types():
    """Explain the difference between result types."""
    
    print("=" * 60)
    print("  LlamaParse — Result Types")
    print("=" * 60)
    
    print("\n  📋 result_type='markdown'")
    print("     Best for: tables, headers, structured content")
    print("     Output preserves table structure as markdown tables")
    
    print("\n  📋 result_type='text'")
    print("     Best for: plain text extraction, simpler processing")
    print("     Strips all formatting, just raw text")
    
    print("\n  ⚠️  LlamaParse requires a LlamaCloud API key")
    print("     Free tier available at: https://cloud.llamaindex.ai")
    print("     Use it when SimpleDirectoryReader gives poor results")


if __name__ == "__main__":
    show_result_types()
    
    if os.getenv("LLAMA_CLOUD_API_KEY"):
        print("\n✅ API key found. You can run the parsing examples.")
        # asyncio.run(parse_complex_pdf())
    else:
        print("\n⚠️  Set LLAMA_CLOUD_API_KEY to run LlamaParse examples.")
