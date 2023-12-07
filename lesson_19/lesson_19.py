# def decorator(func):
#     def wrap():
#         print(f'start')
#         func()
#         print(f'finish')
#     return wrap
#
#
# def summ():
#     print(10+20)


# wrapper = decorator(summ)
# wrapper()
# print('****')
# summ()
# print('****')

# @decorator
# def default():
#     print(50)
#
# default()

# def bold(f):
#     def wrap():
#         return "<b>" + f() + "</b>"
#     return wrap
#
#
# def italic(f):
#     def wrap():
#         return "<li>" + f() + "</li>"
#     return wrap
#
# @italic
# @bold
# def my_text():
#     return 'Hello'
#
#
# print(my_text())

# def decor_with_param(f):
#     def wrap(arg):
#         print(f'this is {f.__name__} and some argument {arg}')
#         print(arg+4)
#         f(arg)
#
#     return wrap
#
#
# @decor_with_param
# def my_custom_func(num):
#     print(num * 2)
#
#
# my_custom_func(5)

# import logging
#
# def logger(func):
#     log = logging.getLogger(__name__)
#
#     def wrapper(a, b):
#         log.info(f'Вызов функции', func.__name__)
#         ret = func(a, b)
#         log.info(f'Вызвана функция', func.__name__)
#         return ret
#
#     return wrapper
#
# @logger
# def add(a,b):
#     print(f'a+b', a + b)
#     return a + b
#
# print(f'start')
# add(10,20)
# add(20,30)
# print(f'finish')

app = {}
def callback(route):
    def wrapper(func):
        app[route] = func

        def wrapped():
            ret = func()
            return ret

        return  wrapped

    return wrapper

@callback('/')
def index():
    print(f'index')
    return True

route = app.get('/')
if route:
    resp = route()
    print(f'answer', resp)
