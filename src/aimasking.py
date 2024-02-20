from openai import AzureOpenAI
import os
import sys
import json
from pprint import pprint

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

client = AzureOpenAI(
    api_key = os.getenv('AZURE_API_KEY'),
    api_version =  "2023-07-01-preview",
    azure_endpoint = "https://ai-proxy.lab.epam.com"
)

def get_completion(prompt, model="gpt-35-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response #.choices[0].message["content"]

def replace_placeholder(prompt_text, input_text):
    return prompt_text.replace("{{INPUT TEXT}}", input_text.strip())

# loading the input prompt file
with open(sys.argv[1], 'r') as prompt_file:
    prompt_text = prompt_file.read()

# loading the input text file
with open(sys.argv[2], 'r') as input_file:
    input_text = input_file.read()

# loading the model
model = sys.argv[3]

# replacing the placeholder with the input from the file
prompt = replace_placeholder(prompt_text, input_text)

completion = get_completion(prompt, model= model, temperature=0)
payload = completion.choices[0].message.content

# print the chat completion
pprint(json.loads(payload), indent=4, width=100)
#pprint(completion)
