import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Check if API key is set
if not API_KEY:
    st.error("⚠️ ERROR: GEMINI_API_KEY is not set in .env!")
    st.stop()

# Configure Google Gemini AI
genai.configure(api_key=API_KEY)

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
    messages = [{"role": "system", "parts": [{"text": SYSTEM_PROMPT}]}]  # Fix API structure

    # Append previous chat history
    if isinstance(history, list) and all(isinstance(msg, tuple) and len(msg) == 2 for msg in history):
        for user_msg, assistant_msg in history:
            messages.append({"role": "user", "parts": [{"text": user_msg}]})
            messages.append({"role": "assistant", "parts": [{"text": assistant_msg}]})

    messages.append({"role": "user", "parts": [{"text": user_input}]})  # Fix input format

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(messages)
        return response.text
    except Exception as e:
        return f"⚠️ Google Gemini API Error: {str(e)}"

# Streamlit UI
st.title("☀️ Solar Industry AI Assistant")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history using Streamlit's chat elements
for user_msg, assistant_msg in st.session_state.chat_history:
    with st.chat_message("user"):
        st.write(user_msg)
    with st.chat_message("assistant"):
        st.write(assistant_msg)

# User Input Box
user_input = st.chat_input("Ask about solar energy...")

if user_input:
    response = call_gemini(user_input, st.session_state.chat_history)
    st.session_state.chat_history.append((user_input, response))
    st.rerun()  # Refresh the UI to display new messages

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()
