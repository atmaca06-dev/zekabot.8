from flask import Flask, request, jsonify
from api_connect import send_to_gpt
import threading

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Zekabot Webhook Sistemi Aktif!"

@app.route("/webhook", methods=["POST"])
def webhook():
    gelen_mesaj = request.form.get("Body")
    print("Gelen mesaj:", gelen_mesaj)  # Takip için

    if gelen_mesaj:
        yanit = send_to_gpt(gelen_mesaj)
        print("Gönderilen yanıt:", yanit)  # Takip için
        return jsonify({"reply": yanit})
    else:
        print("Gelen mesaj boş!")
        return "Mesaj alınamadı", 400

if __name__ == "__main__":
    threading.Thread(target=lambda: print("Zekabot webhook aktif")).start()
    app.run(host="0.0.0.0", port=10000)
