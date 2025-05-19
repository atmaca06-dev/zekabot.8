import os
from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

# Ortam değişkenini yükle (Render ortamında .env yoksa bile sorun olmaz)
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
                {"role": "system", "content": "Zekabot'un kontrol motorusun. Gelen verileri analiz et."},
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
    gelen_mesaj = request.form.get("Body")
    if gelen_mesaj:
        yanit = send_to_gpt(gelen_mesaj)
        return jsonify({"reply": yanit})
    return "Mesaj alınamadı", 400
