import openai
import os
import sys

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]

def replace_placeholder(prompt_text, input_text):
    return prompt_text.replace("{{INPUT TEXT}}", input_text.strip())

# loading the input prompt file
with open(sys.argv[1], 'r') as prompt_file:
    prompt_text = prompt_file.read()

# loading the input text file
with open(sys.argv[2], 'r') as input_file:
    input_text = input_file.read()

# replacing the placeholder with the input from the file
prompt = replace_placeholder(prompt_text, input_text)

# print the chat completion
print(get_completion(prompt, temperature=0))
