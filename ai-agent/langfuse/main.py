# Drop-in replacement to get full logging by changing only the import
from langfuse.openai import OpenAI
 
# Configure the OLLAMA client to use http://localhost:11434/v1 as base url 
client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
)
 
response = client.chat.completions.create(
  model="deepseek-r1:7b", # YOUR MODEL
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who was the first person to step in the USA?"},
    {"role": "assistant", "content": "Columbus made three further voyages to the Americas, exploring the Lesser Antilles in 1493, Trinidad and the northern coast of South America in 1498"},
    {"role": "user", "content": "What were his first words when he stepped on the America?"}
  ]
)
print(response.choices[0].message.content)