import os
from openai import AzureOpenAI
import json
import requests
from dotenv import load_dotenv
load_dotenv()

key=os.getenv("openai_key_speech")
endpoint_url=os.getenv("endpoint_speech")
whisper_model=os.getenv("whisper_model")
chat_model=os.getenv("chat_model")
region=os.getenv("region")

final_url = f"{endpoint_url}/openai/deployments/{whisper_model}/audio/transcriptions?api-version=2023-09-01-preview"

headers = {
    "api-key": key,
}

file_path = "/home/user/MySpace/AzureOpenAI/voicedata/voice.mp4"

# Open the file in binary mode and close it after reading
with open(file_path, "rb") as file:
    files = {"file": (os.path.basename(file_path), file, "application/octet-stream")}

    final_response = requests.post(final_url, headers=headers, files=files).json()
    print(final_response)
    
    user_prompt=final_response['text']
    
    client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint=endpoint_url,
    api_key=key
    )

    completion = client.chat.completions.create(
    model=chat_model,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_prompt}
    ]
    )
  
    print(completion.choices[0].message.content)