from datetime import datetime


def debug(func):
    def wrapper(*args):
        print(f'Func name: ({func.__name__}), argument {args}')
        print(func(*args))
        print(f'finish')
        

    return wrapper


@debug
def summ(a, b):
    result = a + b
    return result


summ(10,5)

def func_time(func):
    def wrapper(self):
        current_time = datetime.now()
        func(self)
        finish_time = datetime.now() - current_time
        print(f'Функция {func.__name__} выполнилась за {finish_time}')

    return wrapper
