import time

import requests
from bs4 import BeautifulSoup

def test():
    header = {
    'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }
    var = "wood"
    URL = "https://in.pinterest.com/search/pins/?q=" + var

    r = requests.get(URL,headers=header)

    soup = BeautifulSoup(r.content, 'html5lib')
    time.sleep(10)
    print(soup)
    alt = []
    src = []

    for link in soup.find_all('img'):
        alt.append(link.get('alt'))
        src.append(link.get('src'))


def main():
    test()


if __name__ == '__main__':
    main()
