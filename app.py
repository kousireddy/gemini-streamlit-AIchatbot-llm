import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

chat = model.start_chat(history=[])

def get_response(user_input):
    response = chat.send_message(user_input)
    return response.text