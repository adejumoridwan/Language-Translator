from utilis import translate
import streamlit as st
import json
import requests
from datetime import datetime

# Strapi API endpoint
STRAPI_URL = "http://localhost:1337/api"


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


# text = "संयुक्त राष्ट्र के प्रमुख का कहना है कि सीरिया में कोई सैन्य समाधान नहीं है"
# a = save_translation(text, translate(text))


def get_history():
    response = requests.get(f"{STRAPI_URL}/translations")
    if response.status_code == 200:
        return response.json()
    return []


# a =get_history()


def main():
    st.title("Language Translator to English with History")

    input_text = st.text_area("Enter the text you want to translate:", height=150)
    if st.button("Translate"):
        if input_text:
            translated_text = translate(input_text)
            st.write("## Translated Text")
            st.write(translated_text)
            save_translation(input_text, translated_text)
        else:
            st.warning("Please enter some text to translate.")

    if st.button("History"):
        history = get_history()
        if history:
            for item in history["data"]:
                st.write(
                    f"**Date:** {item['attributes']['translation_date']}\n"
                    f"**Input:** {item['attributes']['input_text']}\n"
                    f"**Translated:** {item['attributes']['translated_text']}"
                )
        else:
            st.write("No history found.")


if __name__ == "__main__":
    main()
