import os
from dotenv import load_dotenv
import chainlit as cl
from litellm import completion
import json


load_dotenv()

gemini_api = os.getenv("GEMINI_API_KEY")
if not gemini_api:
    raise ValueError("GEMINI_API_KEY is missing in .env.")

@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("chat_history", [])
    await cl.Message(content="Welcome to the **Translator Agent**!\n\nPlease tell me **what you want to translate** and **into which language**.").send()

    
@cl.on_message
async def on_message(message: cl.Message):
    msg = cl.Message(content="Translating...")
    await msg.send()
    
    
    history = cl.user_session.get("chat_history") or []
    history.append({"role": "user", "content": message.content})
    
    try:
        response = completion(
            model="gemini/gemini-1.5-flash",
            api_key=gemini_api,
            # provider="google/ai-studio",
            # api_base="https://generativelanguage.googleapis.com/v1beta",
            messages=history 
        )
        response_content = response.choices[0].message.content
        msg.content = response_content
        await msg.update()
        history.append({"role": "assistant", "content" : response_content})
        cl.user_session.set("chat_history", history)
    except Exception as e:
        msg.content = f"Error : {str(e)}"
        await msg.update()
        
        
@cl.on_chat_end
async def on_chat_end():
    history = cl.user_session.get("chat_history") or []
    
    with open("translation_chat_hisory.json", "w") as f:
        json.dump(history, f , indent=2)
    print("chat history saved.")
