import requests
from bs4 import BeautifulSoup
from openai import OpenAI
import os

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def veri_cek(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")
        baslik = soup.find("h1")
        return baslik.text.strip() if baslik else "Başlık bulunamadı."
    except Exception as e:
        return f"Veri çekme hatası: {str(e)}"

def gpt_analiz_et(veri):
    try:
        yanit = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Sen web sitelerinden gelen içerikleri analiz eden gelişmiş bir yapay zekâsın."},
                {"role": "user", "content": f"Bu içeriği analiz et:\n\n{veri}"}
            ]
        )
        return yanit.choices[0].message.content
    except Exception as e:
        return f"GPT analiz hatası: {str(e)}"

def analiz_yap(url):
    veri = veri_cek(url)
    return gpt_analiz_et(veri)
