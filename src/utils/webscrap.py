import requests
from bs4 import BeautifulSoup
import time


#  get phonetic from web
def word_request(word):
    r = requests.get(f'https://easypronunciation.com/en/english/word/{word}')
    if r.status_code == requests.codes.ok :
        Html_content = r.content
        soup = BeautifulSoup(Html_content, "html.parser")
        phonetic = soup.h4.get_text()
        return phonetic
    else:
        print(f'Request to {word} is not successily!')
    time.sleep(10)


if __name__ == '__main__':
    word_request('instance')

