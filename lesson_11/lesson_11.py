import random

# a = (1,2,3,4)
# b = [1,2,3,4]

# print(a.__sizeof__())
# print(b.__sizeof__())

# list_1 = [1,2,3,4]
# t_to_list = list(list_1)
# print(t_to_list)
# t_to_list.append(50)
# print(t_to_list)
# list_1 = tuple(t_to_list)
# print(list_1)

# tuple_1 = tuple(random.randint(0,101) for i in range(10))
# print(tuple_1)

# t = ('hello', 'world','1')
# print(','.join(t))

# Даны два кортежа:
# A = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
# B = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
# Ȁеобходимо определить:
# 1) Ȅумма элементов какого из кортежей больше и вывести
# соответствующее
# сообщение на экран ( Ȅумма больше в кортеже - ..)
# 2) Вывести на экран порядковые номера минимальных элементов этих
# кортежей


# A = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
# B = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
#
# sum_a = sum(A)
# sum_b = sum(B)
#
# if sum_a > sum_b:
#     print(f'Cумма больше в кортеже - A')
# else:
#     print(f'Cумма больше в кортеже - B')
#
# a_min = min(A)
# b_min = min(B)
# print(A.index(a_min),B.index(b_min))

# my_list = [1,2,3,4,5,5,7,3,4,5,6,7,7,3,3,2,2]
# my_set = set(my_list)
# new_list = list(my_set)
# if my_list == new_list:
#     print('False')
# else:
#     print('True')

# my_list = [12,3,4,5,46,54,7,45,64,64,64,32,42,32312]
# my_set = set(my_list)
# print(my_set)
# my_fr_set = frozenset(my_set)
# myfr_set_new = frozenset((300,400,500))
# new_set = my_set.union(my_fr_set)
# print(new_set)
# new_set_section = my_set.intersection(my_fr_set)
# print(new_set_section)





