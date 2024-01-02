import sqlite3

# Создать 2 таблицы в Базе Данных
# Одна будет хранить текстовые данные(1 колонка) Другая числовые(1 колонка)
# Есть список, состоящий из чисел и слов.
# Если элемент списка слово, записать его в соответствующую таблицу, затем посчитать длину слова и записать её в числовую таблицу
# Если элемент списка число: проверить, если число чётное записать его в таблицу чисел, если нечётное, то записать во вторую таблицу слово: «нечётное»
# Если число записей во второй таблице больше 5, то удалить 1 запись в первой таблице. Если меньше, то обновить 1 запись в первой таблице на «hello»

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS texts (text_column TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS numbers (number_column INTEGER)''')

my_list = [5, 'apple', 10, 'banana', 'orange', 3, 'grape', 8, 'kiwi']

for item in my_list:
    if isinstance(item, str):
        cursor.execute('''INSERT INTO texts (text_column) VALUES (?)''', (item,))

        length = len(item)
        cursor.execute('''INSERT INTO numbers (number_column) VALUES (?)''', (length,))

    elif isinstance(item, int):
        if item % 2 == 0:
            cursor.execute('''INSERT INTO numbers (number_column) VALUES (?)''', (item,))
        else:
            cursor.execute('''INSERT INTO texts (text_column) VALUES (?)''', ('нечётное',))

cursor.execute('''SELECT COUNT(*) FROM texts''')
count = cursor.fetchone()[0]

if count > 5:
    cursor.execute('''DELETE FROM texts WHERE ROWID = (SELECT MIN(ROWID) FROM texts)''')
else:
    cursor.execute('''UPDATE texts SET text_column = ? WHERE ROWID = 1''', ('hello',))

cursor.execute('''SELECT * FROM texts''')
data_texts = cursor.fetchall()

conn.commit()
