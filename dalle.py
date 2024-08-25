# Note: DALL-E 3 requires version 1.0.0 of the openai-python library or later
import os
from openai import AzureOpenAI
import json
from dotenv import load_dotenv
load_dotenv()

endpoint=os.getenv("endpoint")
key=os.getenv("openai_key")

client = AzureOpenAI(
    api_version="2024-05-01-preview",
    azure_endpoint=endpoint,
    api_key=key,
)

result = client.images.generate(
    model="Dalle3", # the name of your DALL-E 3 deployment
    prompt="Generate a image that a man is playing with dog",
    n=1
)

image_url = json.loads(result.model_dump_json())['data'][0]['url']

print(image_url)
