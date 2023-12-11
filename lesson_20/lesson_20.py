import datetime
import logging
import time


# e = [1,2,3,4,5]
# e_i = iter(e)
# print(e_i)
#
# print(next(e_i))

# class IterExample:
#     def __iter__(self):
#         self.x = 0
#         return self
#
#     def __next__(self):
#         if self.x <= 100:
#             y = self.x
#             self.x += 1
#             return y
#         else:
#             raise StopIteration
#
# class_instance = IterExample()
# elem = iter(class_instance)
#
# print(next(elem))
# print(next(elem))
# print(next(elem))
#
# for i in elem:
#     print(i)

#----------------------

# elms = [2, 7, 3, 4, 5, 6]
# def my_sqrt(num):
#     for i in num:
#         yield i ** 2
#
#
# s = my_sqrt(elms)
# print(s)
# print(next(s))
# print(next(s))
#
# s_1 = (i ** 2 for i in elms)
# print(s_1)
# print(next(s_1))
# print(next(s_1))
#
# s_1 = (i ** 2 for i in elms)
# s_11 = [i ** 2 for i in elms]
#
# print(s_1, type(s_1))
# print(s_11, type(s_11))

#----------------------

def decor(v):
    def decorwrap(func):
        def wrap(x):
            t1 = datetime.datetime.now()
            res = func(x)
            t2 = datetime.datetime.now() - t1
            if v:
                print(t2)
            return res

        return wrap

    return decorwrap


@decor(v=True)
def my_func(x):
    time.sleep(1)
    print(f'value -> {x}')


my_func(15)