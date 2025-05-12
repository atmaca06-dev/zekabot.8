import requests
from bs4 import BeautifulSoup

def scrape_data():
    url = "https://httpbin.org/html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print("Veri çekildi:", soup.find('h1').text)
