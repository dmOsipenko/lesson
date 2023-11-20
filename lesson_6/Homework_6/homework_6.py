import random

#1 Перемножить все нечётные значения в диапазоне от 1 до 30.
# result = 1
#
# for item in range(1,31,2):
#     result *= item
# print(result)

#Записать в массив все числа в диапазоне от 1 до 100 кратные 5

# lst = []
#
# for item in range(1,101):
#     if item % 5 == 0:
#         lst.append(item)
# print(lst)

 #Вывести на экран все чётные значения в диапазоне от 1 до 71

# even = ""
# for item in range(1,71):
#     if item % 2 == 0:
#         even += str(item) + ","
# even = even[:-1]
# print(even)


#Дан массив чисел. Если число встречается более двух раз, то добавить его в новый массив
# lst_number = []
# lst_filtered = []
# # Рандомно наполняем массив
# for item in range(0,15):
#     lst_number.append(random.randint(0,6))
# print(lst_number)
#
# for item in lst_number:
#     if lst_number.count(item) > 2:
#         if item not in lst_filtered:
#             lst_filtered.append(item)
# print(lst_filtered)