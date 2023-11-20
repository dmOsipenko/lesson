# def func():
#     print('Hello')
# lst = [1,2,3,4,45,5,6,66]
# res = 1
# def summ(lst: list, res: int):
#     for item in lst:
#         res += item
#     print(res)
#
# summ(lst, res)

# def summ():
#     res = 1
#     for item in range(1,21):
#         res += item
#     print(res)
# summ()

# def add(a,b):
#     print(a+b)
#
# add(1,2)

# def func_1():
#     global a
#     a = 1
#     b = 2
#     return  a+b
#
# def func_2():
#     c = 3
#     return a+c
#
# print(func_1())
# print(func_2())

# def func_3(a,b): return a+b

# product = lambda x,y : x+y
# print(product(2,2))
#
# pwd = lambda  a = 2,b = 3: a*b

# def is_year_leap(year):
#     return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
#
# print(is_year_leap(2022))

# import math
# def sqrt(side):
#     p = side * 4
#     s = side * 2
#     d = math.sqrt(2)*side
#     return p,s,d
# print(sqrt(2))

# def seson(month):
#    if 3<=month<6:
#        season_name = 'spring'
#    elif 6<=month<9:
#        season_name = 'summer'
#    elif 9<=month<12:
#        season_name = 'autm'
#    elif 1<=month<3:
#        season_name = 'winter'
#    else:
#        season_name = 'mistake'
#    return season_name
#
# print(seson(6))

def is_prime():
    for item in range(0,100):
        if not item % 2 == 0:
             print(item)

is_prime()