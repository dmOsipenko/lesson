import json
# Задача No1
# Пользователь будет вводить название и стоимость каждой своей покупки за день, до тех пор пока он не напишет “стоп”.
# Ваша задача записать это в json файл в формате:
# {"название" : "яблоко", "стоимость": "200"}
# Задача No2
# Прочитать файл из предыдущего задания и вывести стоимость всех покупок за день

def create_json():
    data = {}
    data['name_product'] = []
    data['price_product'] = []
    while True:
        name_product = input(f'Введите название товара: ')
        if name_product == 'stop':
            break
        price_product = int(input(f'Введите стоимость: '))
        data['name_product'].append(name_product)
        data['price_product'].append(price_product)
    print(data)
    with open('data_product.json','w') as file:
        json.dump(data,file)

def open_json():
    with open('data_product.json') as file:
        data = json.load(file)
        result = 0
        for item in data['price_product']:
            result += item
        print(f'Стоимость всех покупок за день: {result}')

create_json()
open_json()