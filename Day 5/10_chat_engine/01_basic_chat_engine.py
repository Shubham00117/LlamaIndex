"""
Topic 10 — Chat Engine
Subtopics #57-60: Chat Engine, Modes, Memory, Chat Stores

Chat Engine is the multi-turn conversational interface.
Unlike QueryEngine (single Q&A), ChatEngine maintains conversation history.

⚠️ Requires: pip install llama-index-core llama-index-llms-openai
"""


def chat_engine_examples():
    """Show chat engine creation and modes."""
    
    basic = '''
# Create a chat engine from index
chat_engine = index.as_chat_engine(
    chat_mode="condense_question",  # Reformulates questions with history
    similarity_top_k=5,
)

# Multi-turn conversation
response1 = await chat_engine.achat("What is LlamaIndex?")
print(response1)

# Follow-up — automatically uses chat history
response2 = await chat_engine.achat("What are its main features?")
print(response2)

# Reset conversation
chat_engine.reset()
'''
    
    modes = '''
# Chat modes:
# "condense_question" — Condenses follow-up into standalone question
chat_engine = index.as_chat_engine(chat_mode="condense_question")

# "context" — Retrieves context + injects chat history into prompt
chat_engine = index.as_chat_engine(chat_mode="context")

# "openai" — Uses OpenAI function calling
chat_engine = index.as_chat_engine(chat_mode="openai")
'''
    
    memory = '''
# Custom chat memory
from llama_index.core.memory import ChatMemoryBuffer

memory = ChatMemoryBuffer.from_defaults(token_limit=3900)

chat_engine = index.as_chat_engine(
    chat_mode="condense_question",
    memory=memory,
)
'''
    
    store = '''
# Persistent chat store (Redis-backed for production)
from llama_index.core.storage.chat_store import SimpleChatStore

chat_store = SimpleChatStore()

# Save and load chat history
chat_store.persist("./chat_store.json")
loaded_store = SimpleChatStore.from_persist_path("./chat_store.json")
'''
    
    print("=" * 60)
    print("  Chat Engine Examples")
    print("=" * 60)
    print("\n📋 Basic Chat Engine:")
    print(basic)
    print("📋 Chat Modes:")
    print(modes)
    print("📋 Custom Memory:")
    print(memory)
    print("📋 Persistent Chat Store:")
    print(store)


if __name__ == "__main__":
    chat_engine_examples()
