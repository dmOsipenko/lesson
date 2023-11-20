#Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# 􏰀трока – кол-во букв.
# 􏰀делать проверку со всеми этими случаями.

def count_checker(data):
    if type(data) == tuple:
        result = ''
        for item in tuple(data):
            result += str(item)
            print(f'{str(item)} - {len(str(item))}')
        print(f'Общая длина слов - {len(result)}')
    elif type(data) == list:
        letter = ''
        numbers = []
        for item in data:
            if type(item) == str:
                letter += item
            else:
                numbers.append(numbers)
        print(f'Колличество букв {len(letter)}')
        print(f'Количество цифр {len(numbers)}')
    elif type(data) == str:
        print(f'Кол-во букв {len("".join(data.split()))}')
    elif type(data) == int:
        number = ''
        for item in str(data):
            if int(item) % 2 != 0:
                number += item
        print(f'Кол-во нечётных цифр {len(number)}')


count_checker(('hello','world','hy'))
count_checker([3,44,'hello','hy'])
count_checker('Dmitry Osipenko')
count_checker(123456)