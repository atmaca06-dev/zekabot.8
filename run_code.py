from .web_scraping import scrape_data
from .api_connect import check_api
from .form_login import perform_login
from .gpt_module import gpt_analysis
from .messaging import send_message
import time

def run_all_tasks():
    while True:
        try:
            scrape_data()
            check_api()
            perform_login()
            gpt_analysis()
            send_message("Görevler başarıyla tamamlandı.")
            print("Tüm görevler başarıyla yürütüldü. 60 saniye bekleniyor...")
        except Exception as e:
            send_message(f"Hata oluştu: {e}")
            print("Hata:", e)
        time.sleep(60)
