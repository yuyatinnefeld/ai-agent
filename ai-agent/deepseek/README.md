# Ollama + DeepSeek Setup

## 1. Run the Ollama with DeepSeek model
```bash
# Set environment variables for the image and model
export MY_IMAGE=deepseek-ollame
export MODEL=deepseek-coder:6.7b
export CONTAINER=ollama

# Build Ollama + DeepSeek Image
docker build --build-arg MODEL=$MODEL -t $MY_IMAGE .

# Run the Ollama container on the created network
docker run --network=mynetwork -d \
  -v ollama:/root/.ollama \
  -p 11434:11434 \
  --name $CONTAINER \
  $MY_IMAGE
```

## 2. Test Deepseek API Response
You can test the response from the Deepseek API (running inside the Docker container) using the following command:
```bash
# Set an alias for the deepseek command
alias deepseek="docker exec -it ollama ollama run $MODEL"

# Send a test message
message="tell me a joke"
deepseek $message
```

```
curl -X POST http://localhost:11434/api/generate -d '{
      "model": "deepseek-r1:7b",
      "prompt": "Tell me about AI.",
      "stream": false
    }' -H "Content-Type: application/json"

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

curl http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ollama" \
  -d '{
    "model": "deepseek-r1:7b",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Who was the first person to step in the USA?"},
      {"role": "assistant", "content": "Columbus made three further voyages to the Americas, exploring the Lesser Antilles in 1493, Trinidad and the northern coast of South America in 1498"},
      {"role": "user", "content": "What were his first words when he stepped on the America?"}
    ]
  }'
```
## 3. Deploy with HelmChart
```bash
# push image
export IMAGE_NAME="yuyatinnefeld/$MY_IMAGE"
docker image tag ${MY_IMAGE} ${IMAGE_NAME}:1.0.0
docker image push ${IMAGE_NAME}:1.0.0

cd deepseek/helm
helm install ollama . -f values.yaml
```
