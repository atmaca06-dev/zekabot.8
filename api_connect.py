import requests

def check_api():
    response = requests.get("https://httpbin.org/get")
    if response.status_code == 200:
        print("API bağlantısı başarılı:", response.json())
    else:
        print("API bağlantısı başarısız")
