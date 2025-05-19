from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

app = Flask(__name__)

def send_to_gpt(mesaj):
    try:
        print("GPT'ye giden mesaj:", mesaj)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Zekabot'sun. Gelen mesajı yorumla ve düzgün cevapla."},
                {"role": "user", "content": mesaj}
            ]
        )
        yanit = response.choices[0].message.content
        print("GPT'den gelen yanıt:", yanit)
        return yanit
    except Exception as e:
        print("GPT Hatası:", e)
        return "GPT bağlantı hatası!"

@app.route("/", methods=["GET"])
def index():
    return "Zekabot Webhook Sistemi Aktif!"

@app.route("/webhook", methods=["POST"])
def webhook():
    print("Webhook'a istek geldi.")
    print("İstek içeriği:", request.form)
    gelen_mesaj = request.form.get("Body")
    if gelen_mesaj:
        yanit = send_to_gpt(gelen_mesaj)
        return yanit
    return "Mesaj alınamadı!", 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
