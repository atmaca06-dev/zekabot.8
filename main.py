import threading
from flask import Flask
from zekacore_zekabot_taks.gpt_connect import gpt_soru_sor

def start_tasks():
    print("Zekabot başlatıldı, GPT'ye bağlanıyor...")
    cevap = gpt_soru_sor("Zekabot Render üzerinden GPT ile iletişime geçti.")
    print("GPT'den Gelen:", cevap)

app = Flask(__name__)

@app.route("/")
def index():
    return "Zekabot GPT bağlantısı çalışıyor!"

if __name__ == "__main__":
    threading.Thread(target=start_tasks).start()
    app.run(host="0.0.0.0", port=10000)
