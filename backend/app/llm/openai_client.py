# app/llm/openai_client.py
import os
from openai import AsyncOpenAI
from dotenv import load_dotenv
from pathlib import Path

# --- Load API Key Securely ---
base_dir = Path(__file__).resolve().parent.parent.parent
env_path = base_dir / ".env"
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    print("❌ ERROR: OPENAI_API_KEY is missing in .env")

# Initialize Async Client
client = AsyncOpenAI(api_key=API_KEY)

# Use 'gpt-3.5-turbo-0125' or 'gpt-4-turbo' which supports JSON mode natively
MODEL_NAME = "gpt-3.5-turbo-0125"

async def call_llm(system_prompt: str, user_prompt: str):
    try:
        response = await client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={"type": "json_object"} # Force valid JSON
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI API Error: {e}")
        return "{}"