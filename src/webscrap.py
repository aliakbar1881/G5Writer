import requests

from bs4 import BeautifulSoup

import time

def request(word):
    try:
        r = requests.get(f'https://easypronunciation.com/en/english/word/{word}')
        print(r.status_code)
        if r.status_code == requests.codes.ok :
            R = r.content
            soup = BeautifulSoup(R, "html.parser")
            print(soup)
            phonetic = soup.h4.get_text()
            print(phonetic)
            return phonetic
        else:
            print(f'Request not succeible:   {word}')
    except Exception  as e :
        print(f'you have a error on :    {word}')

        print(e)
    else:
        print(f'request succesed :    {word}')
    finally:
        time.sleep(25)

if __name__ == '__main__':
    print('__main__')
    request('instance')
