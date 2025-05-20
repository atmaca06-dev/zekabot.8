from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def send_to_gpt(mesaj):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Sen Zekabot'sun. Kullanıcıya etkili ve detaylı cevaplar ver."},
                {"role": "user", "content": mesaj}
            ]
        )
        yanit = response.choices[0].message.content
        model_adi = response.model
        return f"{yanit}\n\n(Kullanılan model: {model_adi})"
    except Exception as e:
        return f"GPT Hatası: {str(e)}"
