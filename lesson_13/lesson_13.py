from datetime import datetime,timedelta
import math

# def bmi(weight, height):
#     result = weight/(height**2)
#     if 18.5 >= result:
#         print(f'недостаток')
#     elif 18.5 < result <= 25:
#         print(f'норма')
#     else:
#         print('ожирение')
#
# bmi(50, 1.78)
#
# def figure(*args):
#     if len(args) == 3:
#         print('3x')
#     elif len(args) == 4:
#         print(f'4x')
#     elif len(args) == 5:
#         print(f'5x')
#     elif len(args) == 6:
#         print(f'6x')
#     elif len(args) == 7:
#         print(f'7x')
#     elif len(args) == 8:
#         print(f'8x')
#     elif len(args) == 9:
#         print(f'9x')
#     elif len(args) == 10:
#         print(f'10x')
#     else:
#         print(f'no figure')
#
# def next_day(day):
#     current_day = datetime.strptime(day,'%d/%m/%Y')
#     next_day = current_day + timedelta(days=1)
#     return next_day.strftime('%d/%m/%Y')
#
# print(next_day('14/05/2023'))
#
#
# def shop(product_count):
#     sum_of_delivery = 0
#     if product_count == 1:
#         sum_of_delivery = 10.95
#     else:
#         sum_of_delivery = 10.95 + (2.95 * (product_count - 1))
#     return sum_of_delivery

# def math_multiply(a,b):
#     d = math.gcd(a,b)
#     return print(f'{a//d},{b//d}')
#
# math_multiply(6,63)

# lst = [1,2,44,55,'hello',55,'Hey',2,'World',76]
#
# def print_array(lst:list):
#     lst_rev = lst.copy()
#     lst_rev.reverse()
#     print(lst_rev)
#     print(lst[::-1])
#     print(
#         sorted([i for i in lst if isinstance(i, int)]) +
#         sorted([i for i in lst if isinstance(i, str)])
#     )
#     print(lst[1:8])
#     del lst[4]
#     print(lst)
#     print(set(lst))
#
# print_array(lst)

# def count_range(lst, min_value, max_value):
#     x = 0
#     for i in lst:
#         if min_value <= i < max_value:
#             x += i
#     return x
#
# print(count_range([0, 5, 9, -1, -8.1, 5, -5, -1,-9, 1], -7,6))

def button_presses(message):

    dic = {
        1: ['.',',','?','!',':'],
        2: ['A', 'B', 'C'],
        3: ['D','E', 'F'],
        4: ['G','H','I'],
        5: ['J','K','L'],
        6: ['M','N','O'],
        7: ['P','Q','R','S'],
        8: ['T','U','V'],
        9: ['W','X','Y','Z'],
        0: [' ']
    }
    # Создание словаря для сопоставления символов с кнопками
    char_to_button = {}
    for key, value in dic.items():
        for char in value:
            char_to_button[char] = str(key) * (value.index(char) + 1)
            print(char_to_button)
    # Преобразование текста пользователя в последовательность кнопок
    sequence = ''
    for char in message:
        char_upper = char.upper()
        if char_upper in char_to_button:
            sequence += char_to_button[char_upper]
    return sequence


# Пример ввода текста и вывод последовательности кнопок
user_input = input("Введите текст: ")
result = button_presses(user_input)
print("Последовательность кнопок:", result)








