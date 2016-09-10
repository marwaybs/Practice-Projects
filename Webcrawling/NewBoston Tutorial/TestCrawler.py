import requests
from bs4 import BeautifulSoup

def trade_spider():
    url = 'http://bsmarway.pythonanywhere.com'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('a'):
        href = "http://bsmarway.pythonanywhere.com" + link.get('href')
        title = link.string
        print(title)
        print(href)
trade_spider()

