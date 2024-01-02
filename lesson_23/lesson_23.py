import sqlite3

con = sqlite3.connect('first.db')

cursor = con.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS first_tab(id INTEGER PRIMARY KEY AUTOINCREMENT,
# col_1 TEXT, col_2 TEXT)''')
#
# cursor.execute('''INSERT INTO first_tab(col_1,col_2) VALUES('Hello','World')''')

# con.commit()

# val_1 = 'Name_1'
# val_2 = 'Surname_1'
# cursor.execute('''INSERT INTO first_tab(col_1,col_2) VALUES(?,?)''', (val_1,val_2))
#
# # con.commit()
#
# cursor.execute('''SELECT * FROM first_tab''')
# data = cursor.fetchall()
# print(data)

# x = 'hello'
# cursor.execute('''SELECT * FROM first_tab WHERE col_1='Hello' ''')
# data_1 = cursor.fetchall()
# print(data_1)
#
# cursor.execute('''SELECT * FROM first_tab WHERE col_1='xzibit' ''')
# data_1 = cursor.fetchall()
# print(data_1)
#
# cursor.execute('''SELECT * FROM first_tab ORDER BY col_1 ''')
# con.commit()
# data_2 = cursor.fetchall()
# print(data_2)

# cursor.execute('''SELECT * FROM first_tab ORDER BY col_3 ''')
# con.commit()
# data_3 = cursor.fetchall()
# print(data_3)

# cursor.execute('''SELECT * FROM first_tab WHERE col_1 LIKE 'h%' ''')
# con.commit()
# data_4 = cursor.fetchall()
# print(data_4)
#
# cursor.execute('''SELECT * FROM first_tab WHERE col_1 LIKE '7%' ''')
# con.commit()
# data_5 = cursor.fetchall()
# print(data_5)
#
# cursor.execute('''DELETE FROM first_tab WHERE id=1''')
# con.commit()
#
# cursor.execute('''DELETE FROM first_tab WHERE col_1='Hello' ''')
# con.commit()

cursor.execute('''UPDATE first_tab SET col_1='optimuspyyyy' WHERE id=3 ''')
con.commit()
cursor.execute('''SELECT * FROM first_tab''')
data_6 = cursor.fetchall()
print(data_6)





