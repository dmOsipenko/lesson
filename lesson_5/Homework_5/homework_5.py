import random

count = 5

while count > 0:
    numbers = int(input(f'Введите число от 1 до 10: '))
    color = input(f'Введите цвет фишки красный или черный: ')
    pc_number = random.randint(1, 10)
    pc_color = random.randint(1, 2)
    change_color = ''
    if pc_color == 1:
        change_color = 'черный'
    else:
        change_color = 'красный'

    if (numbers == pc_number) and (color == change_color):
        print(f'Вы выйграли, ваши комбинации совпали!')
        break
    else:
        count -= 1
        if count == 0:
            print(f'Вы проиграли, у вас не осталось попыток')
        else:
            print(f'Упс, вы не угадали... Выигрышная комбинация {pc_number}, {change_color}. У вас осталось {count}/5')