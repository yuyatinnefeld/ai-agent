# Python FastAPI AIChatBot
This project integrates FastAPI with an AI backend (Deepseek + OLLAMA API) to create an AI-powered chatbot.


## 1. Create a Docker Network
Create a custom Docker network so that both FastAPI and Deepseek API can communicate seamlessly.

```bash
# Create a Docker network for FastAPI and Deepseek to share
docker network create mynetwork

# Check the subnet IP of the network
docker network inspect mynetwork | grep Subnet

# Example Output: "Subnet": "172.18.0.0/16"
```

You can use the subnet details to set the DEEPSEEK_API_URL in your application (e.g. FastAPI App):

```
DEEPSEEK_API_URL="http://172.18.0.2:11434/api/generate"
```

## 2. Run Deepseek (Ollama) Backend Service
Run the Deepseek API (or Ollama backend service) in a Docker container on the created network.
- [Ollama Setup](/ai-agent/deepseek/README.md)


## 3. Run FastAPI Frontend Service
Now, let's build and run the FastAPI frontend container.
- [FastAPI Setup](/ai-agent/fastapi/README.md)