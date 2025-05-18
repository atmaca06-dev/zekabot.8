from flask import Flask, request
import openai
import os
from dotenv import load_dotenv

# Ortam değişkenlerini yükle
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

# GPT’ye mesaj gönderme fonksiyonu
def send_to_gpt(mesaj):
    try:
        yanit = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sen Zekabot’sun. Kısa ve net cevap ver."},
                {"role": "user", "content": mesaj}
            ]
        )
        return yanit['choices'][0]['message']['content']
    except Exception as e:
        return f"[HATA] {str(e)}"

from flask import Flask, request
import openai
import os
from dotenv import load_dotenv

# Ortam değişkenlerini yükle
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

# GPT’ye mesaj gönderme fonksiyonu
def send_to_gpt(mesaj):
    try:
        yanit = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sen Zekabot’sun. Kısa ve net cevap ver."},
                {"role": "user", "content": mesaj}
            ]
        )
        return yanit['choices'][0]['message']['content']
    except Exception as e:
        return f"[HATA] {str(e)}"

@app.route("/webhook", methods=["POST"])
def webhook():
    gelen_mesaj = request.form.get("Body")
    if gelen_mesaj:
        yanit = send_to_gpt(gelen_mesaj)
        return yanit, 200
    else:
        return "No message received", 400

# Basit test sayfası
@app.route("/")
def index():
    return "Zekabot Webhook Aktif!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)


# Basit test sayfası
@app.route("/")
def index():
    return "Zekabot Webhook Aktif!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
