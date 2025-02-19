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

# AI Behavior Prompt (Added to User's First Message Instead of a System Role)
AI_INSTRUCTIONS = """You are a Solar Industry Expert AI Assistant. 
Provide accurate and professional information about:
- Solar Panel Technology
- Installation Processes
- Maintenance Requirements
- Cost & ROI Analysis
- Industry Regulations
- Market Trends

Tailor responses based on the user's technical level. Decline non-solar-related questions politely."""

# Function to Call Google Gemini AI
def call_gemini(user_input, history):
    messages = []  # Gemini only supports "user" and "model" roles

    # Add AI instructions only once at the start of conversation
    if not history:
        messages.append({"role": "user", "parts": [{"text": AI_INSTRUCTIONS}]})

    # Append previous chat history
    if isinstance(history, list) and all(isinstance(msg, tuple) and len(msg) == 2 for msg in history):
        for user_msg, model_msg in history:
            messages.append({"role": "user", "parts": [{"text": user_msg}]})
            messages.append({"role": "model", "parts": [{"text": model_msg}]})  # Fixed "assistant" -> "model"

    # Add new user message
    messages.append({"role": "user", "parts": [{"text": user_input}]})

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
for user_msg, model_msg in st.session_state.chat_history:
    with st.chat_message("user"):
        st.write(user_msg)
    with st.chat_message("model"):  # Fixed "assistant" -> "model"
        st.write(model_msg)

# User Input Box
user_input = st.chat_input("Ask about solar energy...")

if user_input:
    response = call_gemini(user_input, st.session_state.chat_history)
    st.session_state.chat_history.append((user_input, response))
    st.rerun()  # Refresh the UI to display new
