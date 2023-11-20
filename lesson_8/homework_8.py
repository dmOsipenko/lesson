

first_number = int(input(f'Введите первое число: '))
operation = input(f'Введите операцию: ')
second_number = int(input(f'Введите второе число: '))

def plus(a,b): return a+b

def minus(a,b): return a-b

def multiply(a,b): return a*b

def divide(a,b): return  a/b

if second_number == 0:
    print(f'На 0 делить нельзя')
else:
    if operation == '+':
        print(plus(first_number,second_number))
    elif operation == "-":
        print(minus(first_number,second_number))
    elif operation == "*":
        print(multiply(first_number,second_number))
    else:
        print(divide(first_number,second_number))
