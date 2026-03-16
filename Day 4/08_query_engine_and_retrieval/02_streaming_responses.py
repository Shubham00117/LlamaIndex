"""
Topic 8 — Query Engine & Retrieval
Subtopic #42: Streaming Responses

Stream tokens as they're generated — essential for chat UIs
that show typing indicators and real-time responses.

⚠️ Requires: pip install llama-index-core llama-index-llms-openai
"""

import asyncio


async def streaming_query():
    """Stream query engine responses."""
    
    code = '''
# Create a streaming query engine
query_engine = index.as_query_engine(streaming=True)

# Stream the response
streaming_response = await query_engine.aquery("Explain RAG")

# Print tokens as they arrive
for token in streaming_response.response_gen:
    print(token, end="", flush=True)

# After streaming, get the full response
print(f"\\nFull response: {streaming_response.response}")
print(f"Source nodes: {len(streaming_response.source_nodes)}")
'''
    
    fastapi_code = '''
# FastAPI streaming endpoint
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.get("/stream")
async def stream_query(q: str):
    streaming_response = await query_engine.aquery(q)
    
    async def generate():
        for token in streaming_response.response_gen:
            yield token
    
    return StreamingResponse(generate(), media_type="text/plain")
'''
    
    print("=" * 60)
    print("  Streaming Query Responses")
    print("=" * 60)
    print(code)
    print("\n📡 FastAPI Streaming Endpoint:")
    print(fastapi_code)


if __name__ == "__main__":
    asyncio.run(streaming_query())
