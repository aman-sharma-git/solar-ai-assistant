import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# AI Behavior Prompt
SYSTEM_PROMPT = """You are a Solar Industry Expert AI Assistant. Provide accurate information about:
- Solar Panel Technology
- Installation Processes
- Maintenance Requirements
- Cost & ROI Analysis
- Industry Regulations
- Market Trends

Tailor responses to the user's technical level. Be professional and polite. Decline non-solar questions."""

# Function to Call Google Gemini AI
def call_gemini(user_input, history):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    if isinstance(history, list) and all(isinstance(msg, tuple) and len(msg) == 2 for msg in history):
        for user_msg, assistant_msg in history:
            messages.append({"role": "user", "content": user_msg})
            messages.append({"role": "assistant", "content": assistant_msg})

    messages.append({"role": "user", "content": user_input})

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(messages)
        return response.text
    except Exception as e:
        return f"⚠️ Google Gemini API Error: {str(e)}"

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
