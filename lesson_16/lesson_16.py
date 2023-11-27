# try:
#     x = 100/0
# except ZeroDivisionError:
#     print(f'На 0 делить нельзя')
#
# print(f'......')

# d = {'name': 'Dima'}
# try:
#     print(d['age'])
# except KeyError:
#     d['age'] = 1
#     print(d['age'])
#
# print(d['age'])

# l = ['hello', 'world']
# try:
#     print(l[2])
# except IndexError:
#     print(f'Будь внимателнее')
#     l.append('!')
#     print(l)
#

# d1 = {'name':'Dima','age':31}

# try:
#     v = d1['city']
# except IndexError:
#     print(f'Index out of range')
# except KeyError:
#     print(f'Key not found')
# except Exception:
#     print(f'BIG ERROR')

# try:
#     v = d1['city']
#     print(v)
# except(IndexError,KeyError):
#     print(f'We are have a problem')

# d1 = {'name':'Dima','age':31}
# try:
#     v = d1['age']
#     print(v)
# except IndexError:
#     print(f'key not found')
# finally:
#     print(f'......')

# d1 = {'name':'Dima','age':31}
# try:
#     v = d1['age']
#     print(v)
# except IndexError:
#     print(f'key not found')
# else:
#     print(f'......')

# n_1 = int(input(f'enter first value: '))
# n_2 = int(input(f'enter second value: '))
#
# try:
#    result = n_1 / n_2
#    print(result ** 2)
# except ZeroDivisionError:
#     print(f'На 0 делить нельзя')
# finally:
#     print("SUCCESS")

# Введите два числа с клавиатуры. Ȃоделите одно на другое.
# ȁбработайте деления на ноль, преобразования и общее исключение.

n_1 = int(input(f'enter first value: '))
n_2 = int(input(f'enter second value: '))

try:
   result = n_1 / n_2
   print(result ** 2)
except ZeroDivisionError:
    print(f'На 0 делить нельзя')
except TypeError:
    print(f'TYPE ERROR')
except Exception:
    print(f'BIG ERROR')
finally:
    print("SUCCESS")