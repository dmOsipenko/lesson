import random
#Задание 1
ann_apple_count = 2
paul_apple_count = 5
print(f'У Анны {ann_apple_count} яблока, а у Пола {paul_apple_count} яблок')

#Задание 2

edge_value = float(input('Введите длину ребра куба: '))
v = edge_value ** 3
s = 6 * edge_value ** 2
print(f'Объем куба = {v}, площадь боковой поверхности = {s}')

#Задание 3
tree_height = 20
snail_path_day = 2
slide_down = 1
number_meters_day = snail_path_day - slide_down
result = tree_height / number_meters_day
print(f'Улитка проползет за {result} дней')

#Творческое задание
#Ввести логин и пароль, после этого пройти проверку что Вы не робот

rand_value = random.randint(1,10)

login = input('Введите ваш логин: ')
password = input('Введите ваш пароль: ')
check_user = int(input(f'Решите задачу: {rand_value} + {rand_value} = '))