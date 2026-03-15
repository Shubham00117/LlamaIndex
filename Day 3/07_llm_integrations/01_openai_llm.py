"""
Topic 7 — LLM Integrations
Subtopic #33: OpenAI (GPT-4o, GPT-4)

OpenAI is the most commonly used LLM provider in LlamaIndex.

⚠️ Requires: pip install llama-index-llms-openai
"""

from llama_index.core import Settings


def setup_openai_llm():
    """Configure OpenAI as the global LLM."""
    
    from llama_index.llms.openai import OpenAI
    
    # GPT-4o — best quality/cost balance
    llm = OpenAI(
        model="gpt-4o",
        temperature=0.1,    # Low temp = deterministic answers
        max_tokens=4096,    # Max output tokens
    )
    
    Settings.llm = llm
    
    # Direct completion (outside of query engine)
    response = llm.complete("Explain RAG in one sentence.")
    print(f"Response: {response.text}")
    
    # Chat interface
    from llama_index.core.llms import ChatMessage
    
    messages = [
        ChatMessage(role="system", content="You are a helpful assistant."),
        ChatMessage(role="user", content="What is LlamaIndex?"),
    ]
    chat_response = llm.chat(messages)
    print(f"Chat: {chat_response.message.content}")
    
    return llm


if __name__ == "__main__":
    print("=" * 60)
    print("  OpenAI LLM Integration")
    print("=" * 60)
    
    print("\n📋 Available models:")
    print("  gpt-4o        → Best quality/cost balance")
    print("  gpt-4o-mini   → Cheapest, still good quality")
    print("  gpt-4-turbo   → Previous gen, 128K context")
    print("  o1-preview     → Reasoning model")
    
    # Uncomment to run (requires OPENAI_API_KEY):
    # setup_openai_llm()
