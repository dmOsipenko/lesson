import random
# def many(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# many(1,2,2,3,4, name='Dima', age=31)

# def factor(x):
#     if x != 0:
#         return x * factor(x-1)
#     else:
#         return 1
#
# print(factor(5))

# def add(a,b):
#     return a + b
#
# print((add(1,2)))
#
# data = add(3,4)
# print(data,type(data))
# print(add,type(add))
#
# add_1 = add
# print(add_1,type(add_1))
#
# add_2 = add_1
# print(add_2,type(add_2))

# def sq(x):
#     return x * x
#
# print(sq(2))
#
# square = sq
# print(square(3))

# def func_1(x):
#     def func_2(y):
#         return x * y
#     return func_2
#
# print(func_1(2)(30))

# def func_4(number):
#     i = 0
#     while number > 0:
#         number = int(number/10)
#         i += 1
#         print(i)
#
# func_4(245)

# Ȁаписать функцию, которая заполняет массив длинной 10
# элементов, случайными числами в диапазоне, указанном
# пользователем с клавиатуры. Функция должна принимать два
# аргумента – начало диапазона и его конец, при этом ничего не
# возвращать.

# Ȁаписать функцию и сделать так, чтобы число секунд
# отображалось в виде дни:часы:минуты:секунды.

# def time(sec):
#     day = sec // (60*60*24)
#     sec = sec % (60*60*24)
#     hour = sec // (60*60)
#     sec = sec % (60*60)
#     minutes = sec // 60
#     sec = sec % 60
#
#     print(f'{day}:{hour}:{minutes}:{sec}')
#
# time(3601)


def letter(text:str):
    g = 0
    s = 0
    const = 'aeiouy'
    for item in text:
        if item.isalpha() and item in const:
            g +=1
        elif item.isdigit():
            continue
        else:
            s +=1
    print(f'g-{g}, s-{s}')

text = input(f'Введитк текст: ')

letter(text)





