from flask import Flask, request
from dotenv import load_dotenv
import os
import openai
from twilio.twiml.messaging_response import MessagingResponse

# Çevre değişkeni yükle
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

app = Flask(__name__)

def send_to_gpt(mesaj):
    try:
        print("GPT'ye gönderilen mesaj:", mesaj)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Zekabot'un kontrol motorusun. Gelen verileri analiz et."},
                {"role": "user", "content": mesaj}
            ]
        )
        yanit = response.choices[0].message.content
        print("GPT yanıtı:", yanit)
        return yanit
    except Exception as e:
        print("GPT Hatası:", e)
        return "GPT bağlantı hatası!"

@app.route("/", methods=["GET"])
def index():
    return "Zekabot Webhook Sistemi Aktif!"

@app.route("/webhook", methods=["POST"])
def webhook():
    gelen_mesaj = request.form.get("Body")
    print("WhatsApp'tan gelen mesaj:", gelen_mesaj)

    yanit = send_to_gpt(gelen_mesaj)

    twiml_cevap = MessagingResponse()
    twiml_cevap.message(yanit)
    return str(twiml_cevap)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
