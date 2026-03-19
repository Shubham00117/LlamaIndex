"""
Topic 19 — Real-World Project Patterns
Subtopics #113-122: Enterprise Q&A, Multi-Doc Research, Chatbot,
Multi-Tenant RAG, Corrective RAG, Full-Stack Apps

Complete project patterns combining multiple LlamaIndex features.
"""


def enterprise_document_qa():
    """Enterprise Document Q&A system (full RAG pattern)."""
    
    code = '''
# ─── Enterprise Document Q&A System ───
# Combines: Ingestion Pipeline + Vector Store + Reranking + Metadata Filtering

import asyncio
from llama_index.core import VectorStoreIndex, Settings
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.postprocessor.cohere_rerank import CohereRerank

# 1. Configure
Settings.llm = OpenAI(model="gpt-4o", temperature=0.1)
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")

# 2. Ingest with pipeline
pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(chunk_size=512, chunk_overlap=50),
        OpenAIEmbedding(),
    ]
)
nodes = await pipeline.arun(documents=documents)

# 3. Build index with external vector store
index = VectorStoreIndex(nodes, storage_context=storage_ctx)

# 4. Query with reranking
reranker = CohereRerank(top_n=5)
query_engine = index.as_query_engine(
    similarity_top_k=20,
    node_postprocessors=[reranker],
)

response = await query_engine.aquery("What were the Q3 results?")
'''
    
    print("=" * 60)
    print("  Enterprise Document Q&A")
    print("=" * 60)
    print(code)


def multi_tenant_rag():
    """Multi-tenant RAG with user-level data isolation."""
    
    code = '''
# ─── Multi-Tenant RAG ───
# Each user's data is isolated via metadata filtering

from llama_index.core.vector_stores import MetadataFilter, MetadataFilters

def create_tenant_query_engine(index, user_id: str):
    """Create a query engine scoped to a specific user."""
    
    filters = MetadataFilters(filters=[
        MetadataFilter(key="user_id", value=user_id),
    ])
    
    return index.as_query_engine(
        filters=filters,
        similarity_top_k=5,
    )

# FastAPI endpoint
@app.post("/query")
async def query(request: QueryRequest, user_id: str = Depends(get_current_user)):
    # Each user only sees their own data
    query_engine = create_tenant_query_engine(index, user_id)
    response = await query_engine.aquery(request.question)
    return {"answer": str(response)}
'''
    
    print("\n" + "=" * 60)
    print("  Multi-Tenant RAG")
    print("=" * 60)
    print(code)


def corrective_rag():
    """Corrective RAG — self-correcting retrieval pipeline."""
    
    code = '''
# ─── Corrective RAG ───
# If initial retrieval quality is low, automatically reformulate and retry

from llama_index.core.workflow import Workflow, step, Event, StartEvent, StopEvent
from llama_index.core.evaluation import RelevancyEvaluator

class CorrectionEvent(Event):
    original_query: str
    reformulated_query: str

class CorrectiveRAGWorkflow(Workflow):
    
    @step
    async def retrieve_and_check(self, ev: StartEvent) -> StopEvent | CorrectionEvent:
        """Retrieve and check quality. If poor, reformulate."""
        query = ev.get("query")
        
        # Initial retrieval
        response = await query_engine.aquery(query)
        
        # Check relevancy
        evaluator = RelevancyEvaluator()
        result = await evaluator.aevaluate_response(
            query=query, response=response
        )
        
        if result.passing:
            return StopEvent(result=str(response))
        else:
            # Reformulate the query
            reformulated = await llm.acomplete(
                f"Reformulate this query for better search results: {query}"
            )
            return CorrectionEvent(
                original_query=query,
                reformulated_query=str(reformulated),
            )
    
    @step
    async def retry_with_correction(self, ev: CorrectionEvent) -> StopEvent:
        """Retry with reformulated query."""
        response = await query_engine.aquery(ev.reformulated_query)
        return StopEvent(result=str(response))
'''
    
    print("\n" + "=" * 60)
    print("  Corrective RAG (Self-Correcting)")
    print("=" * 60)
    print(code)


if __name__ == "__main__":
    enterprise_document_qa()
    multi_tenant_rag()
    corrective_rag()
    
    print("\n💡 These patterns combine multiple topics:")
    print("   • Ingestion (Topic 3) + Vector Stores (Topic 5)")
    print("   • Reranking (Topic 9) + Metadata Filtering (Topic 4)")
    print("   • Workflows (Topic 13) + Evaluation (Topic 16)")
    print("   • FastAPI (Topic 18) + Chat Engine (Topic 10)")
