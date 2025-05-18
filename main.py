from flask import Flask, request
import openai
import os
from dotenv import load_dotenv

# Ortam değişkenlerini yükle
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

# GPT’ye mesaj gönderme fonksiyonu
def send_to_gpt(mesaj):
    try:
        yanit = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sen Zekabot’sun. Kısa ve net cevap ver."},
                {"role": "user", "content": mesaj}
            ]
        )
        return yanit['choices'][0]['message']['content']
    except Exception as e:
        return f"[HATA] {str(e)}"

# Twilio'dan gelen mesajı yakala
@app.route("/webhook", methods=["POST"])
def webhook():
    gelen_mesaj = request.values.get("Body", "")
    yanit = send_to_gpt(gelen_mesaj)
    return yanit

# Basit test sayfası
@app.route("/")
def index():
    return "Zekabot Webhook Aktif!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
