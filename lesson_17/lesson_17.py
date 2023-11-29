import math
# class Car:
#     default_color = 'red'
#     # color:str
#     def __init__(self,color):
#         self.color = color
#
#     def turn_on(self):
#         return 'Hello'
#
#     def ride(self):
#         return self.color
#
# car_obj = Car(color='blue')
# print(car_obj.color)

# class Apple:
#     def __init__(self, amount):
#         self.amount = amount
#
#     def eat(self, n):
#         self.amount -= n
#         return self.amount
#
# apple = Apple(amount=10)
# print(apple.amount)
# print(apple.eat(5))

# Создайте класс Example. В нём пропишите 3 (метода) функции. Две
# переменные задайте статически, две динамически.
# Ȃервая функция: создайте переменную и выведите её
# Вторая функция: верните сумму 2-ух глобальных переменных
# Третья функция: верните результат возведения первой динамической
# переменной во вторую динамическую переменную
# Создайте объект класса.
# Ȁапечатайте обе функции
# Ȁапечатайте переменную a

# class Example:
#     a = 5
#     b = 10
#     def __init__(self, c,d):
#         self.c = c
#         self.d = d
#
#
#     def func_1(self):
#         self.f = 100
#         return self.f
#
#     def func_2(self):
#         return self.a + self.b
#
#     def func_3(self):
#         return self.c ** self.d
#
# exam = Example(c=7,d=8)
#
# # print(exam.func_1())
# print(exam.func_1())
# print(exam.f)
# print(exam.func_2())
# print(exam.func_3())
# print(exam.a)


# Калькулятор.
# Создайте класс, где реализованы функции(методы) математических
# операций. А также функция, для ввод данных.

class Calculator:

    def __init__(self,a,b,sign):
        self.a = a
        self.b = b
        self.sign = sign
    def plus(self):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def result(self):
        if self.sign == '+':
            return self.plus()
        elif self.sign == '-':
            self.minus()
        elif self.sign == '*':
            self.multiply()
        elif self.sign == '/':
            self.division()
        else:
            print('Error')

calculator = Calculator(a=int(input(f'Введите первое число: ')),
                        b=int(input(f'Введите второе число: ')),
                        sign=input(f'Введите математическое действие: '))
print(calculator.result())


