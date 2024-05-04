import requests
import os
from dotenv import load_dotenv

load_dotenv()

HUGGING_FACE_TOKEN = os.getenv("HUGGING_FACE_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/facebook/mbart-large-50-many-to-one-mmt"
headers = {"Authorization": f"Bearer {HUGGING_FACE_TOKEN}"}

text = "संयुक्त राष्ट्र के प्रमुख का कहना है कि सीरिया में कोई सैन्य समाधान नहीं है"


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


translate(text)

