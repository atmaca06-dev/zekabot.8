from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

def send_to_gpt(mesaj):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sen Zekabot'un kontrol motorusun. Verileri analiz et."},
                {"role": "user", "content": mesaj}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        print("GPT hatası:", e)
        return "GPT bağlantı hatası"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    mesaj = data.get("Body") or data.get("message")
    yanit = send_to_gpt(mesaj)
    return jsonify({"reply": yanit})

@app.route("/")
def index():
    return "Zekabot webhook aktif!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
