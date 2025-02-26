# ☀️ Solar Industry AI Assistant

## 🌍[App Link](https://solar-ai-assistant-ekpyo5.streamlit.app/)

This project is a **Solar Industry AI Assistant** built using **Streamlit** and **Google Gemini AI**. It provides users with accurate and professional information about solar energy.

---

## 📚 Project Structure

- **`.env`** – Stores the API key for Google Gemini AI.
- **`app.py`** – The main Python script that runs the Streamlit application.
- **`requirements.txt`** – Lists the dependencies required to run the project.

---

## 📥 Installation

### **1️⃣ Install Dependencies**
Run the following command in **Windows PowerShell** or **Terminal**:
```bash
pip install -r requirements.txt
```

### **2️⃣ Set Up API Key**
- Get an **API Key** from [Google Gemini AI](https://ai.google.com/).
- Add it inside the **`.env`** file:
  ```plaintext
  GEMINI_API_KEY="your_api_key_here"
  ```
- **⚠️ Do not share or expose your API key publicly!** 🧑‍🔧
- If this key is missing, the app will show an error and **stop execution**.

---

## 🚀 Running the Application
Once everything is set up, start the project using:
```bash
streamlit run app.py
```
This will open the **Solar Industry AI Assistant** in your web browser.

---

## 🛠️ Features & Functionality

### ✅ **AI-Powered Solar Industry Expert**
The AI provides expert guidance on:
- 🌞 Solar Panel Technology
- 🛠️ Installation Processes
- ⚙️ Maintenance Requirements
- 💰 Cost & ROI Analysis
- 📝 Industry Regulations
- 📈 Market Trends

### ✅ **Solar-Specific Responses**
- The AI will **only** answer solar-related questions.
- If a user asks about unrelated topics, it politely refuses.

### ✅ **Enhanced Contextual Understanding**
- Uses **solar-specific keywords** to determine relevance.
- Recognizes contextual words like **"it"**, **"this"**, **"that"**, ensuring continuity.

### ✅ **Interactive Web UI (Streamlit)**
- Users can input questions.
- Chat history is displayed for reference.
- Buttons for **clearing chat** and **checking chat history**.

### ✅ **Error Handling**
- Ensures the **API Key** is set up before execution.
- Displays a **clear error message** if API calls fail.

---

## 🖥️ Code Overview

### **🔹 Load API Key**
```python
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
```

### **🔹 Define AI Instructions**
```python
AI_INSTRUCTIONS = """You are a Solar Industry Expert AI Assistant.
Provide accurate and professional information about:
- Solar Panel Technology
- Installation Processes
- Maintenance Requirements
- Cost & ROI Analysis
- Industry Regulations
- Market Trends

Only answer questions related to solar energy. If a question is not related to solar, politely refuse to answer."""
```

### **🔹 Check If Question is Solar-Related**
```python
SOLAR_KEYWORDS = ["solar", "photovoltaic", "pv", "renewable energy", "sun",
                  "solar panel", "net metering", "solar cell", "solar inverter",
                  "solar energy", "solar power", "solar battery"]

RELATED_WORDS = ["it", "this", "that", "they", "them", "these", "those"]

def is_solar_related(user_input, history):
    user_input = user_input.lower().split()
    if any(keyword in user_input for keyword in SOLAR_KEYWORDS):
        return True
    return history and any(word in RELATED_WORDS for word in user_input) and is_solar_related(history[-1][0], [])
```

### **🔹 Call Google Gemini AI**
```python
def call_gemini(user_input, history):
    messages = [{"role": "user", "parts": [{"text": AI_INSTRUCTIONS}]}] if not history else []
    
    messages.extend(
        [{"role": "user", "parts": [{"text": msg[0]}]}, {"role": "model", "parts": [{"text": msg[1]}]}]
        for msg in history
    )
    
    messages.append({"role": "user", "parts": [{"text": user_input}]})
    
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(messages)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {e}"
```

### **🔹 Streamlit Web UI**
```python
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
```

---

## 🧪 Testing the Application
Try asking **solar-related** questions like:
✅ "What are the benefits of solar panels?"
✅ "How do I install a solar inverter?"
❌ If you ask **non-solar** questions, the AI will refuse to answer.

---

## 🐝 Contributing
If you want to contribute:
1. **Fork** the repository.
2. Create a **new branch** (`feature-branch`).
3. **Commit** your changes.
4. **Push** and submit a **pull request**.

---

## 📢 License
This project is open-source. Feel free to modify and improve it!

---

## 💍 Useful Links
- [Google Gemini API Docs](https://ai.google.com/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [GitHub Repository](https://github.com/aman-sharma-git/solar-ai-assistant)

Happy coding! 🚀

