"""
LlamaIndex Example: Async Programming Basics
--------------------------------------------
Production LlamaIndex systems are almost entirely ASYNC. All major components 
(Query Engines, Chat Engines, Agents, Readers) expose async variants to ensure 
high performance and non-blocking I/O in production environments.

Key Async Methods:
  - query_engine.aquery()   → Asynchronous query execution
  - chat_engine.achat()     → Asynchronous chat interaction
  - agent.arun()            → Asynchronous agent run/task
  - reader.aload_data()     → Asynchronous document loading

Best Practice: Always use async in FastAPI, workflows, and production APIs 
to avoid blocking the main thread's event loop.

Requirements:
  pip install llama-index-core llama-index-llms-openai
"""

import asyncio


# -------------------------------------------------------------
# Example 1: Sync vs Async Query (Concept Demonstration)
# -------------------------------------------------------------

def sync_query_example(query_engine, question: str) -> str:
    """
    ❌ SYNC — Blocks the event loop.
    
    This method should be avoided in production APIs (FastAPI, Flask, etc.) 
    as it prevents the server from handling other concurrent requests.
    Only use in simple CLI scripts or Jupyter notebook explorations.
    
    Args:
        query_engine: The LlamaIndex query engine instance.
        question: The user query string.
        
    Returns:
        The text response from the query engine.
    """
    response = query_engine.query(question)
    return str(response)


async def async_query_example(query_engine, question: str) -> str:
    """
    ✅ ASYNC — Non-blocking.
    
    The recommended approach for production. This allows the event loop 
    to handle other tasks while waiting for LLM or Vector Store responses.
    
    Args:
        query_engine: The LlamaIndex query engine instance.
        question: The user query string.
        
    Returns:
        The text response from the query engine.
    """
    response = await query_engine.aquery(question)
    return str(response)


# -------------------------------------------------------------
# Example 2: FastAPI Integration Pattern
# -------------------------------------------------------------

def create_fastapi_app():
    """
    Demonstrates the standard production pattern for integrating 
    LlamaIndex within the FastAPI framework using async endpoints.
    
    Returns:
        A string containing the code template for a FastAPI app.
    """
    
    # NOTE: This is a code template showing the architectural pattern.
    fastapi_code = '''
from fastapi import FastAPI
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

# --- Configure Global Settings at startup ---
# Settings is a singleton object used to configure the LLM and Embedding Model globally.
Settings.llm = OpenAI(model="gpt-4o", temperature=0.1)
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")

# --- Initialize Application State ---
# These would typically be loaded from a vector database in production.
documents = SimpleDirectoryReader("./data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

# --- Create FastAPI application ---
app = FastAPI()

@app.get("/query")
async def query_endpoint(q: str):
    """Async endpoint - non-blocking query execution."""
    response = await query_engine.aquery(q)
    return {
        "answer": str(response),
        "sources": [node.metadata for node in response.source_nodes]
    }

@app.get("/health")
async def health():
    """Basic health check endpoint."""
    return {"status": "ok"}
'''
    
    print("\n📄 FastAPI + LlamaIndex Integration Template:")
    print("-" * 40)
    print(fastapi_code)
    print("-" * 40)
    return fastapi_code


# -------------------------------------------------------------
# Example 3: Common Async Methods Reference
# -------------------------------------------------------------

def show_async_methods():
    """Prints a definitive reference of common async methods in LlamaIndex."""
    
    print("=" * 60)
    print("  LlamaIndex — Definitive Async Method Reference")
    print("=" * 60)
    
    methods = {
        "aquery()": "Async query on QueryEngine (RAG retrieval + LLM synthesis)",
        "achat()": "Async chat on ChatEngine (maintains conversation state)",
        "arun()": "Async execution for Agents & Workflows",
        "aload_data()": "Async document loading from various sources",
        "astream_chat()": "Async streaming for low-latency chat responses",
        "astream_query()": "Async streaming for low-latency query responses",
    }
    
    for method, description in methods.items():
        print(f"\n  🔹 {method}")
        print(f"     {description}")
    
    print("\n⚡ TIP: In standalone scripts, wrap your logic in an async main() function")
    print("   and run it using `asyncio.run(main())`.")


# -------------------------------------------------------------
# Example 4: Running Async Code from a Script
# -------------------------------------------------------------

async def main():
    """
    The entry point for executing asynchronous LlamaIndex operations
    from a standard Python environment.
    """
    
    print("=" * 60)
    print("  Initializing Async LlamaIndex Execution")
    print("=" * 60)
    
    # Prototype for real-world usage:
    # ---------------------------------------------------
    # docs = await SimpleDirectoryReader("./data").aload_data()
    # index = VectorStoreIndex.from_documents(docs)
    # query_engine = index.as_query_engine()
    # res = await query_engine.aquery("How do I use async?")
    
    print("\n✅ Script Pattern: asyncio.run(main())")
    print("✅ Notebook Pattern: await engine.aquery(...) (Jupyter is naturally async)")
    
    show_async_methods()
    create_fastapi_app()


if __name__ == "__main__":
    # The standard way to bootstrap an async Python application
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nExiting...")
