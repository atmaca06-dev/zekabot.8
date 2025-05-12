import threading
from flask import Flask
from zekacore_zekabot_taks.run_code import run_all_tasks

# Görevleri arka planda başlat
def start_tasks():
    print("Zekabot Render üzerinde başlatıldı, görevler yürütülüyor...")
    run_all_tasks()

# Web sunucusu (Render'ı kandırmak için)
app = Flask(__name__)

@app.route("/")
def index():
    return "Zekabot arka planda çalışıyor!"

if __name__ == "__main__":
    # Arka plan görevini başlat
    threading.Thread(target=start_tasks).start()

    # Flask sunucusunu çalıştır (Render için zorunlu)
    app.run(host="0.0.0.0", port=10000)
