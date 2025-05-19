from dotenv import load_dotenv
import os
import openai

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key


def send_to_gpt(mesaj):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sen Zekabot’un denetleyici yapay zekasısın. Görev sonuçlarını analiz et ve gerekli geri bildirimi ver."},
                {"role": "user", "content": mesaj}
            ]
        )
        yanit = response["choices"][0]["message"]["content"]
        return yanit
    except Exception as e:
        return f"[Hata] GPT yanıtı alınamadı: {e}"
