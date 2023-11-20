import random

import requests
import json
import os

# Make the GET request to the horoscope API
# response = requests.get("https://magnacanvas.com/collections/abstract-wall-art.json")
# data = response.json()  # Convert the response to JSON

# Store the JSON data in a file
with open("/Users/dm.osipenko/Desktop/data/datattt.json", "w") as file:
    json.dump('data', file)

# with open("data.json", "r") as file:
#    data = json.load(file)

# Access and process the retrieved JSON data
#date = data

# products_count = data['collection']['products_count']
# print(products_count)

# Print the retrieved data
#print(f"Horoscope for date {date}")

# my_list = [random.randint(0,100) for i in range(6)]
# my_list1 = [i*100 for i in range(6)]
# print(my_list)

# lst = ['hello', 33, True, 34]
# lst.append('world')
# lst.insert(2,"!!!")
# lst[2] = 'ЗАМЕНА'
# print(lst)
# del lst[2] #удаляет по индексу
# print(lst)
# lst.remove(33)  #удаляет значение
# print(lst)

# ll = [1,2,3,['11','22'],False]
# del ll[3][0]
# print(ll)
# ll = [1,2,3,['11','22'],False]
# del ll[0:3]
# print(ll)

# ll = [1,2,3,['11','22'],False]
#
# if 2 in ll:
#     print("YES")
# else:
#     print("NO")

# l1 = [1,2,3]
# l2 = [4,5,6]
# res = l1+l2
# print(res)
#
# l1.append(l2)
# print(l1)
# l3 = [7,8,9]
# l2.extend(l3)
# print(l2)

# my_l1 = [1,2,3]
# my_l2 = my_l1.copy()
# print(my_l1, id(my_l1))
# print(my_l2, id(my_l2))

# lst = [random.randint(0,50) for i in range(6)]
# print(lst)
# print(lst[::-1])
# print(lst.reverse())
#
# lst = [2,3,56,20,54,20,6]
#
# if 20 in lst:
#    index = lst.index(20)
#    lst.insert(index, 200)
# print(lst)

# a = [4,6,'pу','tell',78]
# b = [44,'hello',56,'exept',3]
# Выполнить следующие операции:
# Ȅложить два списка
# Добавьте элемент 6 на 3 позицию.
# Удалите все текстовые переменные
# Ȃосчитайте количество элементов списка

# a.extend(b)
# a.insert(3, 6)
# for item in a:
#    if isinstance(item,str):
#    # if type(item) == str:
#       a.remove(item)
# print(a)