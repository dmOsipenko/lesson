import json

import requests
import os
from bs4 import BeautifulSoup



def get_categories(url):
    page_count = 297 // 19
    result_url_list = []
    for page in range(1, page_count):
        r = requests.get(url=f'{url}?page={page}')
        soup = BeautifulSoup(r.text,"html.parser")
        products = soup.find('div',id='CollectionAjaxResult').find('div',id='CollectionAjaxContent').findAll('div',class_='grid__item grid-product small--one-half medium-up--one-quarter grid-product__has-quick-shop')
        for item in products:
            link = 'https://wallfix.net'+item.find('a',class_='grid-product__link').get('href')
            url_string = link.replace('collections/all/','')
            result_url_list.append({
                'url': url_string
            })
    with open('wallfix_result_url.json', 'w') as file:
        json.dump(result_url_list, file, indent=4, ensure_ascii=False)

def get_images():
    images = []
    with open('wallfix_result_url.json') as file:
        scr = json.load(file)
        for item in scr:
            r = requests.get(url=item.get('url'))
            soup = BeautifulSoup(r.text, "html.parser")
            title = soup.find('h1',class_='h2 product-single__title')
            description = soup.find('div', class_='collapsible-content__inner rte')
            urls = []
            url_images = soup.find('div', class_='grid').find('div', class_='product__thumbs--scroller').findAll('div', class_='product__thumb-item')
            for item in url_images:
                urls.append({
                    'url': f'https:{item.find("a", class_="product__thumb js-no-transition").get("href")}'
                })
            images.append({
                'title': f'{title.text}',
                'description': f'{description.text}',
                'url': urls
            })

    with open('images.json', 'w') as file:
        json.dump(images, file, indent=4, ensure_ascii=False)
def download_images(file_path):
    try:
        with open(file_path) as file:
            data_arr = json.load(file)
    except Exception as _ex:
        print(_ex)
        return f'Check file_path!!!'

    count_name = 1
    if not os.path.exists(f'data'):
        os.mkdir(f'data')

    for item in data_arr[0:51]:
        for i in item.get('url'):
            r = requests.get(url=i.get('url'))
            with open(f"/Users/dm.osipenko/Desktop/wallfix/{count_name}.png", "wb") as file:
                file.write(r.content)
            count_name += 1



def main():
    # get_categories("https://wallfix.net/collections/all")
    # get_images()
    download_images('images.json')


if __name__ == '__main__':
    main()