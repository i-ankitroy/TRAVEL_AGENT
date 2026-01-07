import os
import google.generativeai as genai
from dotenv import load_dotenv
from pathlib import Path

# 1. Get the absolute path to the backend folder (where this file is located, then up 2 levels)
# app/llm/gemini_client.py -> app/llm -> app -> backend
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = BASE_DIR / ".env"

# 2. Load the .env file explicitly
load_dotenv(dotenv_path=ENV_PATH)

# 3. Get the key
API_KEY = os.getenv("GEMINI_API_KEY")

# Debugging: Print this to your terminal to see if it worked
print(f"DEBUG: Looking for .env at: {ENV_PATH}")
if API_KEY:
    print("DEBUG: API Key found successfully.")
else:
    print("DEBUG: API Key is MISSING or None.")

if not API_KEY:
    raise ValueError(f"No API_KEY found! Checked file: {ENV_PATH}")

genai.configure(api_key=API_KEY)

MODEL_NAME = "gemini-1.5-flash"

async def call_llm(system_prompt: str, user_prompt: str):
    try:
        model = genai.GenerativeModel(
            model_name=MODEL_NAME,
            system_instruction=system_prompt,
            generation_config={"response_mime_type": "application/json"}
        )
        response = model.generate_content(user_prompt)
        return response.text
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return "{}"