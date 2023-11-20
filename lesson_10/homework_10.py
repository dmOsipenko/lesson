#У вас есть словарь, где ключ – название продукта. Значение – список, который содержит цену и кол-во товара.
# Выведите через ‘’–’’ название – цену – количество.
# С клавиатуры вводите название товара и его кол-во.
# n – выход из программы. Посчитать цену выбранных товаров и сколько товаров осталось в изначальном списке.

n = True
all_price = 0

products = {
    'bread':[5,1000],
    'cheese':[10,500],
    'meat':[15,600],
    'fish':[22,300]
}

def price_products(price,count):
    global all_price
    result = price * count
    all_price += result
    return print(f'общая стоимость - {all_price} руб')

def result_product():
    for i in products:
        print(f'{i} - цена:{products[i][0]} руб - количество:{products[i][-1]}шт')
def func(product_name: str, products_count: int):
    global n
    for item in products:
        if product_name == item:
            if products[product_name][-1] - products_count >= 0:
                result = products[product_name][-1] - products_count
                products[product_name][-1] = result
                result_product()
                price_products(products[product_name][0], products_count)
            else:
                print('У нас нет столько товара')

result_product()

while n:
    products_name = input(f'Введите название товара(для выхода из программы введите n): ')
    if products_name == 'n':
        n = False
        break
    for item in products:
        if products_name == item:
            products_count = int(input(f'Введите количество: '))
            func(products_name, products_count)
            break
        else:
            print(f'У нас нет такого продукта')
            break


