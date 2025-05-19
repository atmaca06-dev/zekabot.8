from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def send_to_gpt(mesaj):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sen Zekabot'un denetleyici yapay zekasısın. Gelen mesajları analiz et."},
                {"role": "user", "content": mesaj}
            ]
        )
        yanit = response.choices[0].message.content
        return yanit
    except Exception as e:
        return f"GPT Hatası: {str(e)}"
