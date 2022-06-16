from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
URL = 'https://dictionary.cambridge.org/dictionary/english/test'
page = requests.get(URL, headers=headers)

with open('test/test.html', 'w', encoding='utf-8') as f:
    print(page.text, file=f)

