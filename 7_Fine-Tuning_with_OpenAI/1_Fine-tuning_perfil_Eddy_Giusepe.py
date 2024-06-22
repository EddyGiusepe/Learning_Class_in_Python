#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""

import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
#openai.api_key  = os.environ['OPENAI_API_KEY']
Eddy_key_openai  = os.environ['OPENAI_API_KEY']

from openai import OpenAI
client = OpenAI(api_key=Eddy_key_openai)

completion = client.chat.completions.create(
    model = "ft:gpt-3.5-turbo-0125:personal:eddybot-training:9Z8yzWhs",
    messages=[
        {"role": "system", "content": "EddyBot é um ChatBot factual que responde cordialmente às perguntas do usuário."},
        {"role": "user", "content": "Qual é a graduação do Eddy Giusepe Chirinos Isidro?"}
    ]
)

response = completion.choices[0].message
print(response)