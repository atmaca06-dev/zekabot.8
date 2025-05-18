import threading
from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Ortam değişkenlerini yükle
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Flask uygulaması
app = Flask(__name__)

# GPT ile doğrudan konuşan fonksiyon
def send_to_gpt(mesaj):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sen Zekabot'un kontrol motorusun. Gelen verileri analiz edip yorumla."},
                {"role": "user", "content": mesaj}
            @app.route("/webhook", methods=["POST"])
    def webhook():
    data = request.get_json()
    gelen_mesaj = data.get("Body", "")
    yanit = send_to_gpt(gelen_mesaj)
    return jsonify({"reply": yanit})

            ]
            
        )
        yanit = response["choices"][0]["message"]["content"]
        print("GPT'den gelen yanıt:", yanit)
        return yanit
    except Exception as e:
        print("GPT Hatası:", e)
        return "GPT bağlantı hatası"

# Web arayüzü kök endpoint
@app.route("/")
def index():
    return "Zekabot Webhook Sistemi Çalışıyor"

# Webhook endpoint'i
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    mesaj = data.get("mesaj", "Mesaj alınamadı")
    gpt_cevap = send_to_gpt(mesaj)
    return jsonify({"gpt_cevap": gpt_cevap})

# Sunucuyu başlat
if __name__ == "__main__":
    threading.Thread(target=lambda: print("Zekabot Webhook Aktif")).start()
    app.run(host="0.0.0.0", port=10000)
     
