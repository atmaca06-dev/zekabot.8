import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def gpt_soru_sor(mesaj):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": mesaj}]
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"Hata oluştu: {e}"
