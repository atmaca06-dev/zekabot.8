from api_connect import send_to_gpt
from web_analysis import analiz_yap

# GPT yanıtı
mesaj = "Zekabot hazır mısın?"
yanit = send_to_gpt(mesaj)
print("[GPT Yanıtı]:", yanit)

# Web veri analizi örneği
url = "https://www.bbc.com/news"
analiz = analiz_yap(url)
print("\n[Web Analizi]:", analiz)
