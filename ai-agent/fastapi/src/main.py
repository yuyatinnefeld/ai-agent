import json
import os
import re
import requests
import logging
from typing import Union, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# Setup logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables with defaults
DEEPSEEK_HOST_URL = os.getenv("DEEPSEEK_HOST_URL", "http://0.0.0.0:0000")
DEEPSEEK_CHAT_API_URL = DEEPSEEK_HOST_URL + "/api/generate"
DEEPSEEK_PROMP_API_URL = DEEPSEEK_HOST_URL + "/v1/chat/completions"
MODEL_NAME = os.getenv("MODEL_NAME", "SELECT-MODEL!")

app = FastAPI()

class Message(BaseModel):
    message: str

class Messages(BaseModel):
    role: str = Field(default="user", description="Role of the message sender")
    content: str = Field(default="Hello!", description="Content of the message")

class ChatRequest(BaseModel):
    model: str = Field(default="deepseek-coder:6.7b", description="Model name")
    messages: List[Messages] = Field(
        default=[
            Messages(role="system", content="You are a helpful service mesh assistant."),
            Messages(role="assistant", content="When Istio is enabled, every pod in the namespace gets an Envoy sidecar proxy. The sidecar proxy intercepts all inbound and outbound traffic for the pod."),
            Messages(role="user", content="you are using istio as SMI provider. how is istio proxy working?")
        ],
        description="List of messages with predefined defaults"
    )

def send_request(url: str, payload: dict) -> dict:
    """ Send a POST request and handle errors """
    headers = {"Content-Type": "application/json"}
    logger.debug(f"Sending POST request to {url} with payload: {json.dumps(payload)}")

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        response_data = response.json()

        raw_response = (
            response_data.get("choices", [{}])[0].get("message", {}).get("content")
            if "choices" in response_data else response_data.get("response", "No response")
        )

        clean_response = re.sub(r'<think>.*?</think>', '', raw_response, flags=re.DOTALL).strip()

        return {"answer": clean_response}

    except requests.exceptions.RequestException as e:
        logger.error(f"Request to API failed: {e}")
        return {"error": "Request to API failed", "details": str(e)}
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return {"error": "Unexpected error", "details": str(e)}

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"Service": "AI ChatBot"}

@app.get("/health")
def health_check():
    logger.info("Health check endpoint accessed")
        
    try:
        response = requests.get(DEEPSEEK_HOST_URL, timeout=1)
        status_code = response.status_code

        return {
            "status": "Ollama is reachable",
            "status_code": status_code
        }

    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to reach Ollama: {e}")
        return {
            "status": "Ollama is unreachable",
            "status_code": "N/A",
            "error": str(e)
        }

@app.post("/chat/v1")
def chat_completions(request: ChatRequest):
    if MODEL_NAME != request.model:
        logger.warning(f"Model mismatch! Expected: {MODEL_NAME}, Received: {request.model}")
        raise HTTPException(status_code=400, detail=f"Invalid model. Expected: {MODEL_NAME}, but received: {request.model}")

    payload = {"model": request.model, "messages": [message.dict() for message in request.messages]}
    return send_request(DEEPSEEK_PROMP_API_URL, payload)

@app.post("/chat/v2")
def chat_api_generate(message: Message):
    if MODEL_NAME is None:
        logger.error("MODEL_NAME is not set in the environment.")
        raise HTTPException(status_code=500, detail="MODEL_NAME is not configured. Check your environment variables or Dockerfile.")
    payload = {"model": MODEL_NAME, "prompt": message.message, "stream": False}
    return send_request(DEEPSEEK_CHAT_API_URL, payload)
