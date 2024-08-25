import os
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()

endpoint=os.getenv("endpoint")
key=os.getenv("openai_key")
deployment=os.getenv("DEPLOYMENT_NAME")
client = AzureOpenAI(
    api_key=key,
    api_version="2024-02-01",
    azure_endpoint=endpoint
)
      
completion = client.chat.completions.create(
    model=deployment,
    messages= [
    {
      "role": "user",
      "content": "What are the differences between Azure Machine Learning and Azure AI services?"
    }],
    max_tokens=800,
    temperature=0.7,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    stream=False
)
print(completion.to_json())