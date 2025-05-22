import os
from flask import Flask, request
from openai import OpenAI
from twilio.rest import Client
import traceback

app = Flask(__name__)

openai_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
twilio_client = Client(os.environ.get("TWILIO_ACCOUNT_SID"), os.environ.get("TWILIO_AUTH_TOKEN"))
twilio_number = os.environ.get("TWILIO_NUMBER")

# --- Kod test fonksiyonu ---
def test_code(kod):
    import io, sys
    old_stdout = sys.stdout
    sys.stdout = mystdout = io.StringIO()
    try:
        exec(kod)
        result = mystdout.getvalue()
        if not result:
            result = "Kod çalıştı, çıktı üretmedi."
    except Exception:
        result = "Kodda hata var:\n" + traceback.format_exc()
    finally:
        sys.stdout = old_stdout
    return result

# --- Kod düzeltme fonksiyonu ---
def fix_code(kod):
    prompt = f"Bu kodda hata var, düzelt: \n{kod}\n"
    completion = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": prompt}]
    )
    return completion.choices[0].message.content.strip()

# --- Siteye giriş / form doldurma (örnek, detayını sen doldur) ---
def site_login(login_info):
    # login_info = {"site": "...", "username": "...", "password": "..."}
    # Burada otomasyon veya selenium kodunu entegre edebilirsin.
    return f"{login_info.get('site', 'Site')} sitesine giriş denendi (örnek fonksiyon)."

# --- Scrape (veri çekme) fonksiyonu ---
def scrape_site(site, query):
    # Gerçek scraping için burada requests + BeautifulSoup kullanılabilir.
    return f"{site} sitesinde '{query}' için örnek sonuç (buraya gerçek veri entegrasyonu yapılacak)."

# --- GPT komut ayrıştırıcı ---
def gpt_command_parser(user_message):
    prompt = f"""
Sen bir komut analizcisisin. Kullanıcının aşağıdaki mesajını çözümle ve çıktıyı JSON olarak üret.
Mevcut komutlar:
- scrape (veri çekme)
- kod_test (kod test etme)
- kod_fix (kod hatası düzeltme)
- site_login (siteye giriş ve form doldurma)
Komut ve parametrelerini şu formatta döndür:
{{"action": "...", "site": "...", "query": "...", "kod": "...", "login_info": {{...}} }}
Kullanıcı mesajı: {user_message}
Eğer komut anlamıyorsan {{"action": "bilinmiyor"}} döndür.
"""
    completion = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": prompt}]
    )
    import json
    try:
        command = json.loads(completion.choices[0].message.content)
    except Exception:
        command = {"action": "bilinmiyor"}
    return command

# --- Webhook (Twilio, WhatsApp, Telegram ile konuşmak için) ---
@app.route("/webhook", methods=["POST"])
def webhook():
    msg = request.values.get("Body", "").strip()
    sender = request.values.get("From", "")
    command = gpt_command_parser(msg)
    action = command.get("action", "")

    if action == "bilinmiyor":
        cevap = "Komut anlaşılamadı veya bilinmiyor."
    elif action == "kod_test":
        kod = command.get("kod", "")
        cevap = test_code(kod)
    elif action == "kod_fix":
        kod = command.get("kod", "")
        cevap = fix_code(kod)
    elif action == "scrape":
        site = command.get("site", "")
        query = command.get("query", "")
        cevap = scrape_site(site, query)
    elif action == "site_login":
        login_info = command.get("login_info", {})
        cevap = site_login(login_info)
    else:
        cevap = "Tanımsız komut."

    # Twilio üzerinden cevap gönder
    twilio_client.messages.create(
        body=cevap,
        from_=twilio_number,
        to=sender
    )
    return "OK", 200  # <-- BU SATIR SADECE VE SADECE WEBHOOK FONKSİYONUNUN İÇİNDE!

# Ana sayfa testi
@app.route("/", methods=["GET"])
def home():
    return "Zekabot GPT Otomasyon Sistemi Aktif", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
