from flask import Flask, request, jsonify
from openai import OpenAI
import os
from dotenv import load_dotenv

# Ortam değişkenlerini yükle
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# OpenAI istemcisi
client = OpenAI(api_key=api_key)

# Flask uygulaması
app = Flask(__name__)

# GPT ile konuşan fonksiyon
def send_to_gpt(mesaj):
    try:
        print("GPT'ye giden mesaj:", mesaj)  # Takip için
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Zekabot'un kontrol motorusun. Gelen verileri analiz et."},
                {"role": "user", "content": mesaj}
            ]
        )
        yanit = response.choices[0].message.content
        print("GPT'den gelen yanıt:", yanit)  # Takip için
        return yanit
    except Exception as e:
        print("GPT Hatası:", e)
        return "GPT bağlantı hatası!"

# Ana endpoint (GET)
@app.route("/", methods=["GET"])
def index():
    return "Zekabot Webhook Sistemi Aktif!"

# Webhook endpoint (POST)
@app.route("/webhook", methods=["POST"])
def webhook():
    gelen_mesaj = request.form.get("Body")
    if gelen_mesaj:
        yanit = send_to_gpt(gelen_mesaj)
        return jsonify({"reply": yanit})
    return jsonify({"reply": "Mesaj alınamadı."})

# Sunucuyu başlat
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
