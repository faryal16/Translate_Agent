# 🌐 Translator Agent

[🟢 Live Demo on Railway](https://translte-agent-a1955.up.railway.app/)

A simple translation assistant built using **Chainlit**, **LiteLLM**, and **Gemini API**. This agent allows users to translate text into various languages in a conversational format.

---

## 🚀 Features

- Supports natural language prompts for translation
- Maintains conversation history during the session
- Automatically saves chat history to a JSON file on session end
- Powered by Google Gemini 1.5 Flash via LiteLLM
- Deployed with [Railway](https://railway.app/)

---

## 🛠️ Tech Stack

- [Chainlit](https://docs.chainlit.io/) – for building the chat UI
- [LiteLLM](https://docs.litellm.ai/) – for unified LLM API access
- Google Gemini API via [Gemini 1.5 Flash](https://deepmind.google/gemini/)
- Python `dotenv` – to manage API keys securely

---

## 📦 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/translator-agent.git
   cd translator-agent
   ```
2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Create a .env file and add your Gemini API key:**

```env
GEMINI_API_KEY=your_gemini_api_key_her
```
4 **Run the app locally:**

```bash
chainlit run tran_agent.py
```
Then visit http://localhost:8000 in your browser.

## 💬 How to Use
After starting the app, you’ll be greeted with a message:

Welcome to the Translator Agent! Please tell me what you want to translate and into which language.

You can then input prompts like:

- "Translate 'Hello, how are you?' into French."

- "Please translate 'Good morning' into Spanish."

- "Translate 'Where is the nearest hospital?' into German."

The model will respond with the translated version.

## 🧠 Session History
- The conversation is stored in chat_history using cl.user_session.

- On session end, chat history is saved to a file:

```pgsql
translation_chat_hisory.json
```
## 📄 File Structure
```bash
tran_agent.py               # Main Chainlit app
.env                 # Environment variables (not committed)
requirements.txt     # Python dependencies
translation_chat_hisory.json  # Saved chat session history
```

## 📤 Deployment
This app is currently live on:

👉 https://translte-agent-a1955.up.railway.app/

**To deploy yourself:**

Push to GitHub

Connect your repo to Railway

Set GEMINI_API_KEY in Railway environment variables

## 📧 License & Author
Created by [Code With Fairy]

MIT License
