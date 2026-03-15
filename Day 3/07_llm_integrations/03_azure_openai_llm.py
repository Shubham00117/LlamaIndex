"""
Topic 7 — LLM Integrations
Subtopic #35: Azure OpenAI (Enterprise Standard)

Azure OpenAI is the enterprise version of OpenAI. Use it when your
company requires Azure compliance, data residency, or SLAs.

⚠️ Requires: pip install llama-index-llms-azure-openai
"""


def setup_azure_openai():
    """Configure Azure OpenAI."""
    
    code = '''
from llama_index.llms.azure_openai import AzureOpenAI
from llama_index.core import Settings

llm = AzureOpenAI(
    engine="gpt-4o",                       # Your deployment name
    azure_endpoint="https://your-resource.openai.azure.com/",
    api_key="YOUR_AZURE_API_KEY",
    api_version="2024-02-15-preview",
)

Settings.llm = llm
'''
    
    print("=" * 60)
    print("  Azure OpenAI Integration")
    print("=" * 60)
    print(code)
    print("🏢 Use Azure OpenAI for enterprise compliance & SLAs.")


if __name__ == "__main__":
    setup_azure_openai()
