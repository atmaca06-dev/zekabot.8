import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# GPT'ye mesaj gönder
def send_to_gpt(mesaj):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sen Zekabot’un denetleyici yapay zekasısın. Görev sonuçlarına analiz et ve gerekli geri bildirimi ver."},
                {"role": "user", "content": mesaj}
            ]
        )
        yanit = response.choices[0].message.content
        print("GPT'den gelen yanıt:", yanit)
        return yanit
    except Exception as e:
        print("GPT bağlantı hatası:", str(e))
        return "GPT bağlantı hatası"
