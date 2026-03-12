"""
Topic 1 — Setup & Project Foundation
Subtopic #3: Async Programming Basics

Production LlamaIndex is almost entirely ASYNC. All major components
expose async variants:
  - query_engine.aquery()   → async query
  - chat_engine.achat()     → async chat
  - agent.arun()            → async agent run
  - reader.aload_data()     → async document loading

Always use async in FastAPI and workflow contexts to avoid blocking
the event loop.

⚠️ Requires: pip install llama-index-core llama-index-llms-openai
"""

import asyncio


# ─────────────────────────────────────────────────────────────
# Example 1: Sync vs Async Query (concept demonstration)
# ─────────────────────────────────────────────────────────────

def sync_query_example(query_engine, question: str) -> str:
    """
    ❌ SYNC — blocks the event loop.
    Avoid this in production APIs (FastAPI, workflows).
    Only use in simple scripts or Jupyter notebooks.
    """
    response = query_engine.query(question)
    return str(response)


async def async_query_example(query_engine, question: str) -> str:
    """
    ✅ ASYNC — non-blocking.
    Use this in production: FastAPI endpoints, workflows, agents.
    """
    response = await query_engine.aquery(question)
    return str(response)


# ─────────────────────────────────────────────────────────────
# Example 2: FastAPI Integration Pattern
# ─────────────────────────────────────────────────────────────

def create_fastapi_app():
    """
    Shows how to integrate LlamaIndex with FastAPI using async.
    This is the standard production pattern.
    """
    
    # NOTE: This is a code template — won't run standalone without
    # actual documents and an API key configured.
    
    fastapi_code = '''
from fastapi import FastAPI
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

# --- Configure Settings at startup ---
Settings.llm = OpenAI(model="gpt-4o", temperature=0.1)
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")

# --- Build index at startup (runs once) ---
documents = SimpleDirectoryReader("./data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

# --- Create FastAPI app ---
app = FastAPI()

@app.get("/query")
async def query_endpoint(q: str):
    """Async endpoint — uses aquery() to avoid blocking."""
    response = await query_engine.aquery(q)
    return {
        "answer": str(response),
        "sources": [node.metadata for node in response.source_nodes]
    }

@app.get("/health")
async def health():
    return {"status": "ok"}
'''
    
    print("📄 FastAPI + LlamaIndex Template:")
    print(fastapi_code)
    return fastapi_code


# ─────────────────────────────────────────────────────────────
# Example 3: Common Async Methods Reference
# ─────────────────────────────────────────────────────────────

def show_async_methods():
    """Print all common async methods in LlamaIndex."""
    
    print("=" * 60)
    print("  LlamaIndex — Common Async Methods")
    print("=" * 60)
    
    methods = {
        "aquery()": "Async query on QueryEngine",
        "achat()": "Async chat on ChatEngine",
        "arun()": "Async run for Agents & Workflows",
        "aload_data()": "Async document loading",
        "astream_chat()": "Async streaming chat responses",
        "astream_query()": "Async streaming query responses",
    }
    
    for method, description in methods.items():
        print(f"\n  🔹 {method}")
        print(f"     {description}")
    
    print("\n⚡ TIP: Use asyncio.run() when calling async code from a plain")
    print("   Python script outside of FastAPI or a running event loop.")


# ─────────────────────────────────────────────────────────────
# Example 4: Running async code from a script
# ─────────────────────────────────────────────────────────────

async def main():
    """
    Demonstrates the pattern for running async LlamaIndex code
    from a standalone Python script.
    """
    
    print("=" * 60)
    print("  Running Async LlamaIndex Code")
    print("=" * 60)
    
    # In a real script, you would do:
    # documents = await SimpleDirectoryReader("./data").aload_data()
    # index = VectorStoreIndex.from_documents(documents)
    # query_engine = index.as_query_engine()
    # response = await query_engine.aquery("What is RAG?")
    
    print("\n✅ Pattern for standalone scripts:")
    print("   asyncio.run(main())  ← wraps your async code")
    print("\n✅ Pattern for Jupyter notebooks:")
    print("   await query_engine.aquery('...')  ← notebooks have an event loop")
    
    show_async_methods()
    create_fastapi_app()


if __name__ == "__main__":
    # This is the correct way to run async code from a script
    asyncio.run(main())
