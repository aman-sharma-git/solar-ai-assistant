# Solar Industry AI Chatbot

## Overview
This is a Streamlit-based AI chatbot powered by Google Gemini API. It provides expert knowledge on solar energy, including solar panel technology, installation, maintenance, costs, regulations, and market trends.

## Features
- **Expert AI Assistance**: Get accurate and detailed responses related to solar energy.
- **Chat History**: View and retain previous conversations.
- **Clear Chat**: Reset the conversation easily.
- **Restricted Queries**: Only allows solar-related questions.
- **Streamlit UI**: Interactive and user-friendly web interface.

## Installation
### Prerequisites
- Python 3.8+
- A Google Gemini API Key

### Setup
1. **Clone the repository**
   ```sh
   git clone https://github.com/aman-sharma-git/solar-ai-chatbot.git
   cd solar-ai-chatbot
   ```

2. **Create a virtual environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a `.env` file in the project root and add:
     ```
     GEMINI_API_KEY=your_google_gemini_api_key
     ```

5. **Run the chatbot**
   ```sh
   streamlit run app.py
   ```

## Deployment
To deploy on Streamlit Cloud:
1. Push the code to a GitHub repository.
2. Connect the repository to Streamlit Cloud.
3. Configure secrets with your API key.
4. Deploy and access via the provided URL.

## Usage
1. Open the chatbot in a browser.
2. Ask any solar-related questions.
3. View chat history or clear it as needed.

## Troubleshooting
- **API Key Error**: Ensure the `.env` file is correctly set up.
- **Chatbot Not Responding**: Restart Streamlit and check logs.



