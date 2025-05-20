from flask import Flask, request, jsonify
from api_connect import send_to_gpt

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Zekabot Webhook Sistemi Aktif!"

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json()
        mesaj = data.get("message", "")
        yanit = send_to_gpt(mesaj)
        return jsonify({"yanit": yanit})
    except Exception as e:
        return jsonify({"hata": str(e)}), 500

if _name_ == "__main__":
    app.run(host="0.0.0.0", port=10000)
