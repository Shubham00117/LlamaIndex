"""
Topic 7 — LLM Integrations
Subtopics #36, #38-40: Groq, Mistral, AWS Bedrock, Google Gemini

Quick reference for additional LLM providers.
"""


def all_llm_providers():
    """Reference for all additional LLM integrations."""
    
    providers = {
        "Groq (Fast Inference)": '''
pip install llama-index-llms-groq

from llama_index.llms.groq import Groq
llm = Groq(model="llama-3.1-70b-versatile", api_key="...")
''',
        "Mistral AI": '''
pip install llama-index-llms-mistralai

from llama_index.llms.mistralai import MistralAI
llm = MistralAI(model="mistral-large-latest", api_key="...")
''',
        "AWS Bedrock": '''
pip install llama-index-llms-bedrock

from llama_index.llms.bedrock import Bedrock
llm = Bedrock(model="anthropic.claude-v2", region_name="us-east-1")
''',
        "Google Gemini / Vertex AI": '''
pip install llama-index-llms-gemini

from llama_index.llms.gemini import Gemini
llm = Gemini(model="models/gemini-pro", api_key="...")
''',
    }
    
    print("=" * 60)
    print("  Additional LLM Providers")
    print("=" * 60)
    
    for name, code in providers.items():
        print(f"\n{'─' * 50}")
        print(f"  🤖 {name}")
        print(f"{'─' * 50}")
        print(code)
    
    print("💡 All providers follow the same pattern:")
    print("   Settings.llm = <provider>(...)")
    print("   Everything else works the same!")


if __name__ == "__main__":
    all_llm_providers()
