#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

API da OpenAI
=============
Aqui mostramos um pequeno exemplo de como usar
a API da OpenAI.
"""

import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
#openai.api_key  = os.environ['OPENAI_API_KEY']
Eddy_key_openai  = os.environ['OPENAI_API_KEY']

from openai import OpenAI
client = OpenAI(api_key=Eddy_key_openai)


response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Eres um asistente muito útil."},
        {"role": "user", "content": "Menciona três países Latinos."}
    ]
)

print(response.choices[0].message.content)
