from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    print("Webhook çağrıldı!")  # Basit test
    return "OK", 200

if __name__ == "__main__":
    app.run()
