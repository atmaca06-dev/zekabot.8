from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import openai

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

app = Flask(__name__)

def send_to_gpt(mesaj):
    try:
        print("GPT'ye giden mesaj:", mesaj)  # TAKİP 1
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Zekabot'un kontrol motorusun. Gelen verileri analiz et."},
                {"role": "user", "content": mesaj}
            ]
        )
        yanit = response.choices[0].message.content
        print("GPT'den gelen yanıt:", yanit)  # TAKİP 2
        return yanit
    except Exception as e:
        print("GPT Hatası:", e)
        return "GPT bağlantı hatası!"

@app.route("/", methods=["GET"])
def index():
    return "Zekabot Webhook Sistemi Aktif!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.form.to_dict()
    gelen_mesaj = request.form.get("Body")
    print("Tüm veri:", data)                 # TAKİP 3
    print("Gelen mesaj:", gelen_mesaj)       # TAKİP 4

    if gelen_mesaj:
        yanit = send_to_gpt(gelen_mesaj)
        print("Yanıt JSON:", yanit)          # TAKİP 5
        return jsonify({"reply": yanit})
    else:
        print("Boş mesaj geldi!")
        return "Mesaj alınamadı", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
