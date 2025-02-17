# Langfuse

Langfuse is an Open Source LLM Engineering Platform for Traces, evals, prompt management and metrics to debug and improve your LLM application.

## Setup
```bash
export LANGFUSE_PUBLIC_KEY=xxx
export LANGFUSE_SECRET_KEY=xxx
export LANGFUSE_HOST="https://cloud.langfuse.com"

curl http://localhost:11434/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "deepseek-r1:7b",
        "max_tokens": 2048,
        "response_format": {
          "type": "text"
        },
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Hello!"
            }
        ]
    }'
```