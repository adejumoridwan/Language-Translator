from utilis import translate, get_history, save_translation
import streamlit as st



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
            for item in reversed(history["data"]):
                st.text(
                    f"Date: {item['attributes']['translation_date']}\nInput: {item['attributes']['input_text']}\nTranslated: {item['attributes']['translated_text']}"
                )
        else:
            st.write("No history found.")


if __name__ == "__main__":
    main()
