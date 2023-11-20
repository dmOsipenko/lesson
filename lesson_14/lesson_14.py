import os
# f = open('new.txt', 'r') #f = open('new.txt', 'r', encoding = 'utf-8') есои нужно раскодировать #regex101.com регулярные выражения
# print(f)
# print(*f)
# f.close()

# with open('new.txt', 'r') as file:
#     # print(file.read(6))
#     # print(file.read())
#     # print(file.readline())
#     # print(file.readlines())

# with open('new.txt', 'w') as file:
#     file.write('hello\n')
#     file.write('world')
#
# # os.rename('new_today.txt','new.txt')
# # os.mkdir('empty_folder_lesson_14')
# os.chdir('empty_folder_lesson_14') #сменить деректорию
# print(os.getcwd())
# # os.makedirs('empty/empty1/empty2')
# os.chdir('..')
# print(os.getcwd())
# os.rmdir('empty_folder_lesson_14/empty/empty1')

# with open('new.txt','r') as file:
#     text = file.read().replace('_',' ').split(' ')
#     result = 0
#     for i in text:
#         if i.isdigit():
#             result += int(i)
#     print(result)

# Файл содержит числа и буквы. Каждый записан в отдельной строке.
# Ȁужно считать содержимое в список так, чтобы сначала шли числа по
# возрастанию, а потом слова по возрастанию их длины.

# with open('task_2','r') as file:
#     s = file.readlines()
#     value = []
#     text = []
#     for item in s:
#         t = item.strip()
#         if t.isdigit():
#             value.append(int(t))
#         else:
#             text.append(t)
#     value.sort()
#     text.sort()
#     value.extend(text)
#     print(value)


# Создать текстовый файл, записать в него построчно данные, которые
# вводит пользователь. ȁкончанием ввода пусть служит пустая строка.

# with open('user_input','w') as file:
#     while True:
#         text = input(f'enter text: ')
#         if text == '':
#             break
#         file.writelines(f'{text}\n')


