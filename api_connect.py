import os
import openai

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# GPT'ye mesaj gönder
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
        print("GPT'den gelen yanıt:", yanit)
        return yanit
    except Exception as e:
        print("GPT'ye bağlanırken hata oluştu:", e)
        return "GPT bağlantı hatası"
