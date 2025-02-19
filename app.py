import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

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
st.title("☀️ Solar Industry AI Assistant")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for user_msg, assistant_msg in st.session_state.chat_history:
    st.chat_message("user").write(user_msg)
    st.chat_message("assistant").write(assistant_msg)

# User Input
user_input = st.text_input("Ask about solar energy...", key="user_input")
if st.button("Submit") and user_input:
    response = call_gemini(user_input, st.session_state.chat_history)
    st.session_state.chat_history.append((user_input, response))
    st.rerun()

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()
