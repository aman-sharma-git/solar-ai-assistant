import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
if API_KEY:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-pro")
else:
    st.error("🚨 API key is missing! Please add your GEMINI_API_KEY to the .env file.")

# Streamlit UI
st.title("🤖 AI Chatbot - Powered by Google Gemini")

# User input
user_input = st.text_area("Enter your message:", "")

if st.button("Generate Response"):
    if user_input:
        try:
            # Correct message format for Gemini API
            response = model.generate_content([
                {"role": "user", "parts": [{"text": user_input}]}
            ])
            
            # Display the AI response
            st.subheader("🤖 AI Response:")
            st.write(response.text)
        
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")
    else:
        st.warning("⚠️ Please enter a message first.")
