import sys
import os

print("--- DIAGNOSTIC START ---")
print(f"1. Python Executable being used: {sys.executable}")

# Test 1: Check Imports
try:
    import dotenv
    from dotenv import load_dotenv
    print("2. SUCCESS: 'python-dotenv' is installed.")
except ImportError as e:
    print(f"2. FAIL: 'python-dotenv' is NOT installed. Error: {e}")

try:
    import google.generativeai as genai
    print("3. SUCCESS: 'google-generativeai' is installed.")
except ImportError as e:
    print(f"3. FAIL: 'google-generativeai' is NOT installed. Error: {e}")

# Test 2: Check API Key
# Try loading from the current folder
load_dotenv() 
key = os.getenv("GEMINI_API_KEY")

if key:
    print(f"4. SUCCESS: API Key found! (Length: {len(key)} characters)")
else:
    print("4. FAIL: API Key is None. The .env file was not found or is empty.")
    print(f"   Looking in: {os.getcwd()}")

print("--- DIAGNOSTIC END ---")