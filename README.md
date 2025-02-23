# AI Agent Quick Lab

Welcome to the AI Agent Quick Lab! This repository contains everything you need to get started with creating and running an AI-powered chatbot using FastAPI and Ollama models.

## Quick Start
```bash
# deploy
kubectl run pod --image yuyatinnefeld/deepseek-ollame:1.0.0

# start deepseek-coder
kubectl exec -it pod -- ollama run deepseek-coder:6.7b
```

## Ollama Models
Explore the available Ollama models:

- [Deepseek-r1 Model](https://ollama.com/library/deepseek-r1)
- [Deepseek-coder Model](https://ollama.com/library/deepseek-coder)
- [LLAMA3.3 Model](https://ollama.com/library/llama3.3)

## FastAPI AI ChatBot
For detailed instructions on setting up the FastAPI-based AI ChatBot, please follow the steps in the [FastAPI ChatBot Setup Guide](ai-agent/README.md).

---

Feel free to explore and modify the AI ChatBot for your own use cases.
