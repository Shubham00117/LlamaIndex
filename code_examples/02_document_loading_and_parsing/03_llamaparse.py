"""
LlamaIndex Example: LlamaParse — Advanced PDF Parsing
---------------------------------------------------
LlamaParse is a state-of-the-art managed parse API that specializes in 
extracting clean, structured data from complex documents that traditional 
PDF readers often fail on.

Ideal For:
  - Tables with complex cell layouts or merged rows.
  - Multi-column scientific papers or financial reports.
  - Documents containing charts, images, and embedded diagrams.
  - Legal contracts with specific structure and formatting.

Core Concept:
  LlamaParse converts complex PDFs into highly structured Markdown. 
  By parsing into Markdown, the structure of tables and headers is preserved, 
  making the document much easier for an LLM to understand during RAG.

Requirements:
  pip install llama-parse
  Sign up for LLAMA_CLOUD_API_KEY at: https://cloud.llamaindex.ai/
"""

import asyncio
import os


async def parse_complex_pdf():
    """
    Standard parsing logic for a complex PDF using LlamaParse.
    Preserves table structure as Markdown tables.
    """
    from llama_parse import LlamaParse
    
    # Configuration for the Parser
    parser = LlamaParse(
        api_key=os.getenv("LLAMA_CLOUD_API_KEY"),
        result_type="markdown",   # "markdown" (structural) or "text" (raw)
        verbose=True,             # Shows real-time progress of parsing
    )
    
    # Asynchronously parse the file
    # This sends the file to the LlamaCloud API for high-quality extraction
    documents = await parser.aload_data("./data/report.pdf")
    
    print(f"📄 Successfully parsed {len(documents)} document(s) with LlamaParse.")
    for doc in documents:
        print(f"   Extraction Preview (200 chars): {doc.text[:200].strip()}...")
    
    return documents


async def parse_with_advanced_options():
    """
    Demonstrates advanced LlamaParse settings to optimize extraction 
    performance and accuracy.
    """
    from llama_parse import LlamaParse
    
    parser = LlamaParse(
        api_key=os.getenv("LLAMA_CLOUD_API_KEY"),
        result_type="markdown",       # Markdown preserves complex structure
        verbose=True,
        language="en",                # Specify the primary document language
        num_workers=4,                # Parallel processing for multiple files
    )
    
    # Handling multiple documents in a single operation
    file_list = [
        "./data/financial_report.pdf",
        "./data/legal_contract.pdf",
    ]
    
    # Check if files exist locally before attempting to parse
    documents = await parser.aload_data(file_list)
    
    print(f"📄 Successfully parsed {len(documents)} high-complexity files.")
    return documents


def use_llamaparse_within_directory_reader():
    """
    Production Strategy: Hybrid Loading.
    Use LlamaParse as a custom extractor for PDFs while letting 
    SimpleDirectoryReader handle standard file types (.txt, .docx, etc.).
    """
    from llama_index.core import SimpleDirectoryReader
    from llama_parse import LlamaParse
    
    # 1. Create the specialized PDF parser
    parser = LlamaParse(
        api_key=os.getenv("LLAMA_CLOUD_API_KEY"),
        result_type="markdown",
    )
    
    # 2. Map file extensions to the custom parser
    file_extractor = {".pdf": parser}
    
    # 3. SimpleDirectoryReader will use LlamaParse for all .pdf files
    # but use its built-in defaults for every other file type.
    documents = SimpleDirectoryReader(
        input_dir="./data",
        file_extractor=file_extractor,  # Injects specialized parser
    ).load_data()
    
    print(f"📄 Hybrid loading complete: {len(documents)} total documents processed.")
    return documents


def show_result_type_comparison():
    """Prints a comparison between result types in LlamaParse."""
    
    print("=" * 60)
    print("  LlamaParse — Extraction Strategy Reference")
    print("=" * 60)
    
    print("\n  📋 result_type='markdown' [RECOMMENDED]")
    print("     - Best For: Scientific papers, spreadsheets, financial reports.")
    print("     - Benefit: Preserves table structure and hierarchical headers.")
    
    print("\n  📋 result_type='text'")
    print("     - Best For: Plain text documents, simple prose.")
    print("     - Benefit: Minimalist extraction with no formatting overhead.")
    
    print("\n💡 Developer Tip: LlamaParse is a managed service with a free tier.")
    print("   Switch to it whenever SimpleDirectoryReader fails on complex layouts.")


if __name__ == "__main__":
    # Reference guide
    show_result_type_comparison()
    
    # API key validation helper
    api_key = os.getenv("LLAMA_CLOUD_API_KEY")
    if api_key:
        print("\n✅ LLAMA_CLOUD_API_KEY detected. System ready for parsing tasks.")
        # asyncio.run(parse_complex_pdf())
    else:
        print("\n⚠️  LLAMA_CLOUD_API_KEY not found in environment.")
        print("   Set this variable to run live LlamaParse examples.")
