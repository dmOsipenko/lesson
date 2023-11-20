import json

import requests
import os
from bs4 import BeautifulSoup



def get_categories(url):

    response = requests.get(url+'.json')
    data = response.json()
    products_count = data['collection']['products_count']
    page_count = products_count // 9

    result_url_list = []

    for page in range(1, page_count + 1):
        r = requests.get(url=f'{url}?page={page}')
        soup = BeautifulSoup(r.text,"html.parser")
        products = soup.find('div',class_='container').findAll('div',class_='relative product_image')
        for item in products:
            url_str = ('https://magnacanvas.com/'+item.find('a').get('href')).strip()
            result_url_list.append({
                'url': url_str
            })
        with open('result_url.json','w') as file:
            json.dump(result_url_list,file,indent=4,ensure_ascii=False)

def get_images():
    images = []
    with open('result_url.json') as file:
        scr = json.load(file)
        for item in scr:
            r = requests.get(url=item.get('url'))
            soup = BeautifulSoup(r.text, "html.parser")
            products = soup.findAll('a',class_='lightbox')
            for item in products[:5]:
                images.append({
                    'image': f'https:{item.get("href")}'
                })
    with open('image.json', 'w') as file:
        json.dump(images, file, indent=4, ensure_ascii=False)

def download_images(file_path):
    try:
        with open(file_path) as file:
            src = json.load(file)
    except Exception as _ex:
        print(_ex)
        return f'Check file_path!!!'

    count_name = 1
    if not os.path.exists('data'):
        os.mkdir(f'data')
        for item in src[0:201]:
            r = requests.get(url=item.get('image'))
            # with open(f'data/{count_name}.png', 'wb') as file:
            with open(f"/Users/dm.osipenko/Desktop/Images/{count_name}.png", "wb") as file:
                file.write(r.content)
            count_name += 1



def main():
    # get_categories("https://magnacanvas.com/collections/artworks")
    # get_images()
    download_images('image.json')


if __name__ == '__main__':
    main()
