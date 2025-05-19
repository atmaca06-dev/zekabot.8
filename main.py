import threading
from flask import Flask, request
import openai
import os
from dotenv import load_dotenv

# Ortam değişkenlerini yükle
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

def send_to_gpt(mesaj):
    try:
        print("GPT'ye giden mesaj:", mesaj)  # LOG EKLENDİ
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sen Zekabot'un kontrol motorusun. Gelen verileri analiz et ve yorumla."},
                {"role": "user", "content": mesaj}
            ]
        )
        yanit = response["choices"][0]["message"]["content"]
        print("GPT'den gelen yanıt:", yanit)  # LOG EKLENDİ
        return yanit
    except Exception as e:
        print("GPT Hatası:", e)
        return "GPT bağlantı hatası!"

@app.route("/")
def index():
    return "Zekabot Webhook Sistemi Çalışıyor!"

@app.route("/webhook", methods=["POST"])
def webhook():

data = request.get_json()
gelen_mesaj = data.get("Body")
if gelen_mesaj:
yanit = send_to_gpt(gelen_mesaj)
return jsonify ({"reply": yanit} )
 return jsonify ({"reply": "Boş mesaj geldi"} )

if __name__ == "__main__":
    threading.Thread(target=lambda: print("Zekabot webhook aktif")).start()
    app.run(host="0.0.0.0", port=10000)
