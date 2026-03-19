"""
Topic 18 — Production Deployment
Subtopics #102-112: FastAPI, Async, Caching, Docker, llama_deploy

Deploy LlamaIndex applications to production.

⚠️ Requires: pip install llama-index-core fastapi uvicorn
"""


def fastapi_rag_api():
    """Complete FastAPI + LlamaIndex production template."""
    
    code = '''
# main.py — Production RAG API
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from contextlib import asynccontextmanager
from llama_index.core import VectorStoreIndex, Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
import os

# --- Global state ---
query_engine = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize resources at startup."""
    global query_engine
    
    # Configure Settings
    Settings.llm = OpenAI(model="gpt-4o", temperature=0.1)
    Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")
    
    # Load index (from vector store in production)
    from llama_index.core import load_index_from_storage, StorageContext
    storage_ctx = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_ctx)
    query_engine = index.as_query_engine(similarity_top_k=5)
    
    yield
    # Cleanup on shutdown (if needed)


app = FastAPI(title="RAG API", lifespan=lifespan)


class QueryRequest(BaseModel):
    question: str
    top_k: int = 5


class QueryResponse(BaseModel):
    answer: str
    sources: list


@app.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    """Query the knowledge base."""
    try:
        response = await query_engine.aquery(request.question)
        return QueryResponse(
            answer=str(response),
            sources=[
                {"text": n.text[:200], "score": n.score}
                for n in response.source_nodes
            ],
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health():
    return {"status": "ok"}

# Run: uvicorn main:app --host 0.0.0.0 --port 8000
'''
    
    print("=" * 60)
    print("  FastAPI + LlamaIndex Production API")
    print("=" * 60)
    print(code)


def docker_template():
    """Dockerfile for LlamaIndex app."""
    
    dockerfile = '''
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
'''
    
    requirements = '''
# requirements.txt
llama-index-core
llama-index-llms-openai
llama-index-embeddings-openai
fastapi
uvicorn
python-dotenv
'''
    
    print("\n🐳 Dockerfile:")
    print(dockerfile)
    print("📦 requirements.txt:")
    print(requirements)


def caching_patterns():
    """Show caching patterns for cost optimization."""
    
    code = '''
# LLM Response Caching
from llama_index.core import Settings

# Enable in-memory cache (default)
Settings.llm_cache = True

# Redis-backed cache (production)
# pip install llama-index-storage-kvstore-redis
from llama_index.storage.kvstore.redis import RedisKVStore
from llama_index.core.llms import LLMCache

cache = LLMCache(kvstore=RedisKVStore(redis_uri="redis://localhost:6379"))
Settings.llm_cache = cache
'''
    
    print("\n⚡ Caching Patterns:")
    print(code)


if __name__ == "__main__":
    fastapi_rag_api()
    docker_template()
    caching_patterns()
