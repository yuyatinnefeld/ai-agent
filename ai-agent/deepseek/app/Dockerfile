# Use the official Ollama image as the base
FROM ollama/ollama

# Set build argument with default value
ARG MODEL=llama3.2:1b

# Persist the argument as environment variable
ENV MODEL=$MODEL

# Copy the entrypoint script into the container
COPY entrypoint.sh /entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /entrypoint.sh

# Set the custom entrypoint
ENTRYPOINT ["/entrypoint.sh"]