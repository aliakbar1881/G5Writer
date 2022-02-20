"""
    Get data from network and parse it.
"""
import requests
from bs4 import BeautifulSoup

from src.utils.sleep import sleep

#  get phonetic from web
@sleep
def word_phonetic(word):
    result = requests.get(f'https://dictionary.cambridge.org/dictionary/english/{word}')
    if result.status_code == 200:
        html_content = result.text
        soup = BeautifulSoup(html_content, "html.parser")
        phonetic = soup.body.find('span', class_="ipa dipa lpr-2 lpl-1").stripped_strings()
    return phonetic


if __name__ == '__main__':
    print(word_phonetic)
    word_phonetic('content')
