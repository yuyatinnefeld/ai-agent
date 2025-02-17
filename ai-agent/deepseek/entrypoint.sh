#!/bin/sh

# Start Ollama server in the background
ollama serve &

# # Wait for server to be ready
# while ! curl -s http://localhost:11434 >/dev/null; do
#   sleep 1
# done

# Pull the model if it doesn't exist
if ! ollama list | grep -q "$MODEL"; then
  ollama pull "$MODEL"
fi

# Keep the container running
wait