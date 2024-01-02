import random
import sqlite3

# con = sqlite3.connect('db')
#
# cursor = con.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS tab(col_1 INTEGER, col_2 TEXT, col_3 TEXT)''')
#
# int_value = int(input(f'Enter value: '))
#
# cursor.execute('''INSERT INTO tab(col_1,col_2,col_3) VALUES(?,'Dima','Osipenko')''',(int_value,))
#
# con.commit()

# cursor.execute('''SELECT * FROM tab''')
# data = cursor.fetchall()
# for item in data[0]:
#     print(item)

# Создайте новую Базу данных.
# Поля: id, 2 целочисленных поля
# Целочисленные поля заполняются рандомно от 0 до 9
# Посчитайте среднее арифметическое всех элементов без
# учёта id
# Если среднее арифметическое больше количества записей в
# БД, то удалите четвёртую запись БД\

# con = sqlite3.connect('db_2')
#
# cursor = con.cursor()
#
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT,
# col_1 INTEGER, col_2 INTEGER)''')
#
# random_value_1 = random.randint(0,10)
# random_value_2 = random.randint(0,10)
#
# cursor.execute('''INSERT INTO tab_2(col_1,col_2) VALUES(?,?)''',(random_value_1,random_value_2))
#
# con.commit()
#
# cursor.execute('''SELECT col_1,col_2 FROM tab_2''')
# data = cursor.fetchall()
#
# value = 0
#
# for item in data:
#     for i in item:
#         value += i
#
# avg = (value/len(data)*2)
# print(avg)
#
# if avg > len(data):
#     cursor.execute('''DELETE FROM tab_2 WHERE id=4''')
# con.commit()
#
# cursor.execute('''SELECT * FROM tab_2''')
# data = cursor.fetchall()
# print(data)

# Создайте новую Базу данных
# Поля: id, 2 целочисленных поля
# Целочисленные поля заполняются рандомно от 0 до 9
# Выберите случайную запись из БД
# Если каждое число данной записи чётное, то удалите эту
# запись, если нечётное, то обновите данные в ней на(2,2)

# con = sqlite3.connect('db_3')
#
# cursor = con.cursor()
#
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_3(id INTEGER PRIMARY KEY AUTOINCREMENT,
# col_1 INTEGER, col_2 INTEGER)''')
#
# random_value_1 = random.randint(0,10)
# random_value_2 = random.randint(0,10)
#
# cursor.execute('''INSERT INTO tab_3(col_1,col_2) VALUES(?,?)''',(random_value_1,random_value_2))
#
# # con.commit()
#
# cursor.execute('''SELECT id FROM tab_3''')
# data = cursor.fetchall()
#
# random_data = random.choice(data)
# cursor.execute('''SELECT col_1, col_2 FROM tab_3 WHERE id=?''', (random_data))
# w = cursor.fetchall()
# print(w)
# l = []
#
# for i in w:
#     for j in str(i):
#         if j.isdigit():
#             j = int(j)
#             l.append(j)
#
# if l[0] % 2 == 0 and l[1] % 2 == 0:
#     cursor.execute('''DELETE FROM tab_3 WHERE id=?''', (random_data))
#     con.commit()
# else:
#     cursor.execute('''UPDATE tab_3 SET col_1=2,col_2=2 WHERE id=?''',(random_data))
#     con.commit()
#
# cursor.execute('''SELECT * FROM tab_3''')
# x = cursor.fetchall()
# print(x)

