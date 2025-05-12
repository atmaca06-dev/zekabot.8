from dotenv import load_dotenv
import os
import openai  # OpenAI modülünü yüklediysen

# .env dosyasını yükle
load_dotenv()

# .env içinden API anahtarını al
api_key = os.getenv("API_KEY")

# OpenAI API'ye anahtarı tanımla
openai.api_key = api_key
