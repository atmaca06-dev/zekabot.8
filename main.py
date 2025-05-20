from flask import Flask, request
from dotenv import load_dotenv
import os
import openai
from twilio.twiml.messaging_response import MessagingResponse

# Ortam değişkenlerini yükle
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

app = Flask(__name__)

# GPT’ye mesaj gönderme fonksiyonu
def send_to_gpt(mesaj):
    try:
        print("GPT’ye gönderilen mesaj:", mesaj)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Zekabot'un kontrol motorusun. Kullanıcının mesajını analiz et ve doğal bir yanıt üret."},
                {"role": "user", "content": mesaj}
            ]
        )
        yanit = response.choices[0].message.content
        print("GPT yanıtı:", yanit)
        return yanit
    except Exception as e:
        print("GPT Hatası:", e)
        return "GPT bağlantı hatası!"

# Web arayüzü testi
@app.route("/", methods=["GET"])
def index():
    return "Zekabot Webhook Sistemi Aktif!"

# Webhook ile gelen mesajı karşıla
@app.route("/webhook", methods=["POST"])
def webhook():
    gelen_mesaj = request.form.get("Body")
    print("WhatsApp'tan gelen mesaj:", gelen_mesaj)

    yanit = send_to_gpt(gelen_mesaj)

    cevap = MessagingResponse()
    cevap.message(yanit)
    return str(cevap)

# Uygulama çalıştırma
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
