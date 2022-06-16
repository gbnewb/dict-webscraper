import requests
from bs4 import BeautifulSoup

URL = 'https://dictionary.cambridge.org/dictionary/english/example'
page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'})

soup = BeautifulSoup(page.content, 'html.parser')

content = soup.find(id='page-content')
ipa_ga = content.find_all('span', class_='ipa dipa lpr-2 lpl-1')

with open('test/test.html', 'w', encoding='utf-8') as f:
    print(page.text, file=f)
    [print(item) for item in ipa_ga]

