import requests
from bs4 import BeautifulSoup


def get(word: str, site='Cambridge'):
    result = {}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
    
    match site:
        case 'Cambridge':
            URL = f'https://dictionary.cambridge.org/dictionary/english/{word}'
            page = requests.get(URL, headers=headers)
            if page.status_code == 404:
                return result
            else:
                result['raw_html'] = page.text
            
            soup = BeautifulSoup(page.content, 'html.parser')

            content = soup.find(id='page-content')
            ipa_ga = content.find_all('span', class_='ipa dipa lpr-2 lpl-1')
    
    return result


def main():
    """A look-up interface
    """
    word = input('Enter the word you want to look up: ')
    with open('test/test.html', 'w', encoding='utf-8') as f:
        print(get(word)['raw_html'], file=f)


if __name__ == '__main__':
    main()
