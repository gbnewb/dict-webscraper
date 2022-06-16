from selenium import webdriver
from bs4 import BeautifulSoup
import requests

def web_ipa(word, site='Cambridge'):
    match site:
        case 'Cambridge':
            webpage = requests.get(f'https://dictionary.cambridge.org/dictionary/english/{word}')

def main():
    word = input('>')