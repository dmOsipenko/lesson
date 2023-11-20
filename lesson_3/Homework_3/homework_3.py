import random

#Задание 1
#Задача угадать число, которое загадал компьютер
random_value = random.randint(1,10)
number = int(input(f'Угадайте число которое загадал ваш соперник (от 1 до 10): '))
approximate_value = number - random_value

if approximate_value == 0:
    print(f"Вы угадали!!! {number} = {random_value}")
elif (approximate_value == -1 or approximate_value == -2) or (approximate_value == 1 or approximate_value == 2):
    print(f"Почти угадали, это было очень рядом!!! {number} != {random_value}")
elif (approximate_value == -3 or approximate_value == -4) or (approximate_value == 3 or approximate_value == 4):
    print(f"Промах, но было рядом!!! {number} != {random_value}")
elif (approximate_value == -5 or approximate_value == -6) or (approximate_value == 5 or approximate_value == 6):
    print(f"Вы не угадали, совсем далеко!!! {number} != {random_value}")
else:
    print(f'У вас проблемы с интуицией {number} != {random_value}')

#Задача 2:
day = int(input(f'Введите день: '))
month = int(input(f'Введите месяц: '))

if (month == 3 and day >= 21) or (month == 4 and day <= 20):
    print('Овен')
elif (month == 4 and day >= 21) or (month == 5 and day <= 21):
        print('Телец')
elif (month == 5 and day >= 22) or (month == 6 and day <= 21):
        print('Близнецы')
elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        print('Рак')
elif (month == 7 and day >= 23) or (month == 8 and day <= 21):
        print('Лев')
elif (month == 8 and day >= 22) or (month == 9 and day <= 23):
        print('Дева')
elif (month == 9 and day >= 24) or (month == 10 and day <= 23):
        print('Весы')
elif (month == 10 and day >= 24) or (month == 11 and day <= 22):
        print('Скорпион')
elif (month == 11 and day >= 23) or (month == 12 and day <= 22):
        print('Стрелец')
elif (month == 12 and day >= 23) or (month == 1 and day <= 20):
        print('Козерог')
elif (month == 1 and day >= 21) or (month == 2 and day <= 19):
        print('Водолей')
else:
    print('Рыбы')

# #Задание 3
point = 0
question_1 = int(input(f'Какого числа, в марте, отмечают международный женский день: '))
question_2 = int(input(f'Какого числа отмечают день защитника Отечества: '))
question_3 = int(input(f'Какого числа отмечают день матери: '))

answer_1 = question_1 == 8
if answer_1:
    point += 1

answer_2 = question_2 == 23
if answer_2:
    point += 1

answer_3 = question_3 == 14
if answer_3:
    point += 1

if point == 0:
    print(f'Вы ничего не знаете, ваш результат {point}/3')
elif point == 1:
    print(f'Очень слабо, ваш результат {point}/3')
elif point == 2:
    print(f'Вы почти прошли тест, ваш результат {point}/3')
else:
    print(f'Вы прошли тест!!!')
