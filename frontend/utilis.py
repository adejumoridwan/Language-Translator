import requests
import os
import json
from datetime import datetime
from dotenv import load_dotenv


load_dotenv(".env")

HUGGING_FACE_TOKEN = os.getenv("HUGGING_FACE_TOKEN")

# Strapi API endpoint
#use this if you are building locally use this
#STRAPI_URL = "http://localhost:1337/api" 

STRAPI_URL = "https://miraculous-confidence-02c5012cfa.strapiapp.com/api"


API_URL = "https://api-inference.huggingface.co/models/facebook/mbart-large-50-many-to-one-mmt"
headers = {"Authorization": f"Bearer {HUGGING_FACE_TOKEN}"}


def translate(inputs):
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    output = query(
        {
            "inputs": inputs,
        }
    )
    return output[0]["generated_text"]


def save_translation(input_text, translated_text):
    data = {
        "data": {
            "input_text": input_text,
            "translated_text": translated_text,
            "translation_date": datetime.now().isoformat(),
        }
    }

    response = requests.post(
        f"{STRAPI_URL}/translations",
        headers={"Content-Type": "application/json"},
        data=json.dumps(data),
    )
    return response.json()


def get_history():
    response = requests.get(f"{STRAPI_URL}/translations")
    if response.status_code == 200:
        return response.json()
    return []
