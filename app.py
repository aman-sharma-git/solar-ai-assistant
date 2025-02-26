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

# AI Behavior Instructions
AI_INSTRUCTIONS = """You are a Solar Industry Expert AI Assistant. 
Provide accurate and professional information about:
- Solar Panel Technology
- Installation Processes
- Maintenance Requirements
- Cost & ROI Analysis
- Industry Regulations
- Market Trends

Only answer questions related to solar energy. If a question is not related to solar, politely refuse to answer."""

# List of Solar-Related Keywords
SOLAR_KEYWORDS = ["solar", "photovoltaic", "pv", "renewable energy", "sun", 
                  "solar panel", "net metering", "solar cell", "solar inverter", 
                  "solar energy", "solar power", "solar battery"]

# Words that need context (like "it", "this", "that")
RELATED_WORDS = ["it", "this", "that", "they", "them", "these", "those"]

# Function to Check if Question is Solar-Related
def is_solar_related(user_input, history):
    user_input = user_input.lower().split()
    if any(keyword in user_input for keyword in SOLAR_KEYWORDS):
        return True
    return history and any(word in RELATED_WORDS for word in user_input) and is_solar_related(history[-1][0], [])


# Function to Call Google Gemini AI
def call_gemini(user_input, history):
    messages = [{"role": "user", "parts": [{"text": AI_INSTRUCTIONS}]}] if not history else []
    messages += [{"role": "user", "parts": [{"text": msg[0]}]}, {"role": "model", "parts": [{"text": msg[1]}]}] for msg in history
    messages.append({"role": "user", "parts": [{"text": user_input}]})
    
    try:
        return genai.GenerativeModel("gemini-pro").generate_content(messages).text
    except Exception as e:
        return f"⚠️ Error: {e}"


# Streamlit UI
st.title("☀️ Solar Industry AI Assistant")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for user_msg, model_msg in st.session_state.chat_history:
    with st.chat_message("user"):
        st.write(user_msg)
    with st.chat_message("model"):
        st.write(model_msg)

# User Input
user_input = st.chat_input("Ask about solar technology...")

if user_input:
    if is_solar_related(user_input, st.session_state.chat_history):
        response = call_gemini(user_input, st.session_state.chat_history)
    else:
        response = "⚠️ Sorry, I can only answer questions related to solar energy."

    st.session_state.chat_history.append((user_input, response))
    st.rerun()

# Buttons Section
col1, col2 = st.columns(2)

with col1:
    if st.button("Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

with col2:
    if st.button("Check History"):
        st.subheader("🔍 Previous Chat History")
        if st.session_state.chat_history:
            for user_msg, model_msg in st.session_state.chat_history:
                with st.expander(f"📌 {user_msg[:50]}..."):
                    st.write(f"**You:** {user_msg}")
                    st.write(f"**AI:** {model_msg}")
        else:
            st.info("No previous chat history available.")
