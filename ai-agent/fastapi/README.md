# FastAPI App

## Run FastAPI Frontend Service
```bash
# Set environment variables for the image and model
export MY_IMAGE=fastapi-chatbot

# Build the FastAPI Docker image
docker build -t $MY_IMAGE .

# Run the FastAPI chatbot container on the created network
docker run --network=mynetwork -d -p 8080:8080 --name $MY_IMAGE $MY_IMAGE
```

## Check API Responses

Once the services are running, you can check the following endpoints:

- Root endpoint: `http://localhost:8080/`
- Health check: `http://localhost:8080/health`
- Swagger UI: `http://localhost:8080/docs`

## Use the Chatbot API
To send messages to the chatbot and get a response, use the /chat endpoint:

```bash
curl -X 'POST' \
  'http://localhost:8080/chat' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "message": "tell me a joke"
  }'
```