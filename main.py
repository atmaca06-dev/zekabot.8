import threading
from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Ortam değişkenlerini yükle (.env dosyasından)
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Flask uygulaması
app = Flask(__name__)

# GPT-4 (veya turbo) ile doğrudan konuşan fonksiyon
def send_to_gpt(mesaj):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sen Zekabot'un kontrol motorusun. Gelen verileri analiz edip yorumla."},
                {"role": "user", "content": mesaj}
            ]
        )
        yanit = response["choices"][0]["message"]["content"]
        return yanit
    except Exception as e:
        print("GPT hatası:", e)
        return "GPT bağlantı hatası!"

# Web arayüzü kök endpoint
@app.route("/")
def index():
    return "Zekabot Webhook Sistemi Çalışıyor!"

# Twilio'dan gelen mesajları işleyen webhook
@app.route("/webhook", methods=["POST"])
def webhook():
    gelen_mesaj = request.form.get("Body")
    if gelen_mesaj:
        yanit = send_to_gpt(gelen_mesaj)
        return jsonify({"reply": yanit})
    return jsonify({"reply": "Mesaj alınamadı."})

# Sunucuyu başlat
if __name__ == "__main__":
    threading.Thread(target=lambda: print("Zekabot webhook aktif")).start()
    app.run(host="0.0.0.0", port=10000)
