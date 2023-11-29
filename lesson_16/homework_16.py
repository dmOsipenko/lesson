# Ввод с клавиатуры. Если строка введённая с клавиатуры – это числа, то поделить первое на второе.
# 􏰀бработать ошибку деления на ноль. Если второе число 0, то программа запрашивает ввод чисел заново.
# 􏰁акже если были введены буквы, то обработать исключение.


try:
    print(f'!!!!')
    num_1 = input(f'enter first number: ')
    num_2 = input(f'enter second number: ')
    if (num_2 and num_1).isdigit():
        result = int(num_1) / int(num_2)
        print(result)
    else:
        print(f'Ошибка! Возможно Вы ввели вместо числа букву, попробуйте заново!')
        num_1 = input(f'enter first number: ')
        num_2 = input(f'enter second number: ')
        result = int(num_1) / int(num_2)
        print(result)
except ZeroDivisionError:
    print(f'На 0 делить нельзя!!! Введите числа заново')
    num_1 = input(f'enter first number: ')
    num_2 = input(f'enter second number: ')
    result = int(num_1) / int(num_2)
    print(result)
except (TypeError, ValueError):
    print(f'Ошибка! Возможно Вы ввели вместо числа букву, попробуйте заново!')
    num_1 = input(f'enter first number: ')
    num_2 = input(f'enter second number: ')
    result = int(num_1) / int(num_2)
    print(result)
