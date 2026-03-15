# Topic 7: LLM Integrations

## Overview
LlamaIndex supports multiple LLM providers. You configure the LLM once via `Settings.llm` and it's used by all query engines, chat engines, and agents.

## Providers
| Provider | Package | Key Feature |
|----------|---------|-------------|
| OpenAI (GPT-4o) | `llama-index-llms-openai` | Best quality, most popular |
| Anthropic (Claude) | `llama-index-llms-anthropic` | Long context (200K tokens) |
| Azure OpenAI | `llama-index-llms-azure-openai` | Enterprise standard |
| Groq | `llama-index-llms-groq` | Fastest inference |
| Ollama | `llama-index-llms-ollama` | Local/offline models |
| Mistral AI | `llama-index-llms-mistral` | Open-weight models |
| AWS Bedrock | `llama-index-llms-bedrock` | AWS ecosystem |
| Google Gemini | `llama-index-llms-gemini` | Multimodal |
