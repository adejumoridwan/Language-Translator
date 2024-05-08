# Weather Forecast Application

**Description:**

This project builds a robust and interactive web application that leverages the strengths of Streamlit, Strapi and a machine learning model from Hugging Face to translate any language to English.

**Key Features:**
- **Streamlit Frontend**- A streamlit frontend that allows users to give input and see the output.
- **Hugging Face Model**- An Hugging Face model that translates given text to English language.
- **Strapi Backend** - A Strapi backend that stores users input and output in a database, this allows users to see previous inputs and outputs.

**Getting Started:**

1. **Prerequisites:**
   - Basic understanding of Python programming.
   - Familiarity with Streamlit, Strapi and Hugging Face.
2. **Installation:**
   - Clone the repository: `https://github.com/adejumoridwan/Language-Translator.git`
   - Install dependencies: `pip install -r requirements.txt`
   - Install [Node.js](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs), [npm](https://nodejs.org/en/learn/getting-started/an-introduction-to-the-npm-package-manager#introduction-to-npm) then Strapi `npx create-strapi-app@latest backend --quickstart`
3. **Run the application:**
   - Change to the backend directory `cd backend` and start the backend server `npm run develop`.
   - Start the Streamlit app: `streamlit run frontend/main.py`
