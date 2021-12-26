import urllib3




def phonetic(i):
    http = urllib3.PoolManager()
    r = http.request('GET', f'https://dictionary.cambridge.org/dictionary/english/{i}')
    site = r.data
    site = site.decode("utf-8")
    print('success')
    if site.find('"ipa dipa lpr-2 lpl-1"') :
        y = site.find('"ipa dipa lpr-2 lpl-1"') + 23
        x = site[y:].find('<')
        return  site[y:y+x]
    else:
        return 'have a phonetic problem in finding phonetic for {i}'

if __name__ == '__main__':
        print(phonetic('important'))
