"""
Topic 15 — Observability & Debugging
Subtopics #87-90: Tracing, Phoenix, Token Counting, Callbacks

Monitor, debug, and track costs of your LlamaIndex pipelines.

⚠️ Requires: pip install llama-index-core
"""


def observability_examples():
    """Show observability and debugging tools."""
    
    token_counting = '''
# Token counting & cost tracking
from llama_index.core.callbacks import CallbackManager, TokenCountingHandler
import tiktoken

# Set up token counter
token_counter = TokenCountingHandler(
    tokenizer=tiktoken.encoding_for_model("gpt-4o").encode,
    verbose=True,
)

# Attach to Settings
from llama_index.core import Settings
Settings.callback_manager = CallbackManager([token_counter])

# After queries, check usage
print(f"Embedding tokens: {token_counter.total_embedding_token_count}")
print(f"LLM prompt tokens: {token_counter.prompt_llm_token_count}")
print(f"LLM completion tokens: {token_counter.completion_llm_token_count}")
print(f"Total LLM tokens: {token_counter.total_llm_token_count}")
'''
    
    phoenix = '''
# Arize Phoenix — full tracing UI
# pip install arize-phoenix openinference-instrumentation-llama-index

import phoenix as px

# Launch Phoenix UI
px.launch_app()

# Set up LlamaIndex instrumentation
from openinference.instrumentation.llama_index import LlamaIndexInstrumentor
from phoenix.otel import register

tracer_provider = register(endpoint="http://localhost:6006/v1/traces")
LlamaIndexInstrumentor().instrument(tracer_provider=tracer_provider)

# Now all LlamaIndex operations are traced!
# Open http://localhost:6006 to see the trace UI
'''
    
    callbacks = '''
# Custom callbacks for monitoring
from llama_index.core.callbacks import CBEventType, EventPayload
from llama_index.core.callbacks.base_handler import BaseCallbackHandler

class MyCallbackHandler(BaseCallbackHandler):
    def on_event_start(self, event_type, payload=None, **kwargs):
        if event_type == CBEventType.LLM:
            print(f"🤖 LLM call started...")
    
    def on_event_end(self, event_type, payload=None, **kwargs):
        if event_type == CBEventType.LLM:
            print(f"✅ LLM call completed!")

Settings.callback_manager = CallbackManager([MyCallbackHandler()])
'''
    
    print("=" * 60)
    print("  Observability & Debugging")
    print("=" * 60)
    print("\n📊 Token Counting:")
    print(token_counting)
    print("🔍 Arize Phoenix Tracing:")
    print(phoenix)
    print("📋 Custom Callbacks:")
    print(callbacks)


if __name__ == "__main__":
    observability_examples()
