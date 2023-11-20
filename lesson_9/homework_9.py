# Дан список list=[15,48,'hello',6,19,'world’].
# Все числа этого списка проверить на чётность. Если число чётное, то посчитать сумму его цифр.
# Если нечётное, то заменить его на 1 в списке.
# Все слова: посчитать количество гласных и согласных. Вывести всё на экран.

my_list = [15,48,'hellooof',6,19,'world']
sum_result = 0
def chek_letter(text):
    s_count = 0
    g_count = 0
    g_en = 'aeiouy'

    for letter in text.lower().strip():
         if letter in g_en:
            g_count += 1
         else:
            s_count += 1
    print(f'Количество согласных букв: {s_count}, количество гласных букв: {g_count}, ->{text}')


for item in my_list:
    if type(item) == int:
        if item % 2 == 0:
            sum_result += item
        else:
            index = my_list.index(item)
            my_list[index] = 1
    else:
        chek_letter(item)
print(my_list)



