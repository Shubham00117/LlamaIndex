"""
Topic 14 — Prompt Engineering
Subtopics #84-86: System Prompts, Templates, Patterns

Customize prompts for query engines, chat engines, and agents.

⚠️ Requires: pip install llama-index-core
"""

from llama_index.core import PromptTemplate


def custom_system_prompts():
    """Customize system prompts for query/chat engines."""
    
    code = '''
# Custom system prompt for chat engine
chat_engine = index.as_chat_engine(
    chat_mode="condense_question",
    system_prompt=(
        "You are a financial analyst assistant. "
        "Always cite your sources and provide data-driven answers. "
        "If you don't know the answer, say so clearly."
    ),
)

# Custom QA prompt for query engine
from llama_index.core import PromptTemplate

qa_prompt = PromptTemplate(
    "Context information is below.\\n"
    "-----\\n"
    "{context_str}\\n"
    "-----\\n"
    "Given the context information and not prior knowledge, "
    "answer the query in a concise, professional tone.\\n"
    "Query: {query_str}\\n"
    "Answer: "
)

query_engine = index.as_query_engine(
    text_qa_template=qa_prompt,
)
'''
    
    refine_prompt = '''
# Custom refine prompt (for "refine" response mode)
refine_prompt = PromptTemplate(
    "The original query is: {query_str}\\n"
    "We have provided an existing answer: {existing_answer}\\n"
    "We have the opportunity to refine the existing answer "
    "(only if needed) with some more context below.\\n"
    "-----\\n"
    "{context_msg}\\n"
    "-----\\n"
    "Given the new context, refine the original answer to better "
    "answer the query. If the context isn't useful, return the original answer.\\n"
    "Refined Answer: "
)

query_engine = index.as_query_engine(
    response_mode="refine",
    refine_template=refine_prompt,
)
'''
    
    print("=" * 60)
    print("  Prompt Engineering")
    print("=" * 60)
    print("\n📋 Custom System & QA Prompts:")
    print(code)
    print("📋 Custom Refine Prompt:")
    print(refine_prompt)
    
    print("💡 Tips:")
    print("  • {context_str} → replaced with retrieved nodes")
    print("  • {query_str}   → replaced with user's question")
    print("  • {existing_answer} → used in refine mode")
    print("  • Always test prompt changes with evaluation!")


if __name__ == "__main__":
    custom_system_prompts()
