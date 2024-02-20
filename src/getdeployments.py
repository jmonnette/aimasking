import os
import json
from pprint import pprint
import requests

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

url = "https://ai-proxy.lab.epam.com/openai/deployments"
headers = {
    "Api-Key": os.getenv('AZURE_API_KEY'),
}

response = requests.get(url, headers=headers)

for model in response.json()['data']:
    pprint(model['id'])
