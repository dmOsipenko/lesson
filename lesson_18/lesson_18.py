# class Car:
#     def __str__(self):
#         return 'Class Car obj'
#     def start(self):
#         print(f'Engine is started')
#
# car = Car()
# print(car)

# class Phone:
#
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model
#
#     def sim_check(self, operator):
#         if self.model == 'q' and operator == 'a1':
#             return 'ok'
#
# ph = Phone('black', 'q')
# print(ph.sim_check('a1'))

# class Meow:
#     @staticmethod
#     def meo():
#         return 'Myo'
#
# print(Meow.meo())

# class Myclass:
#     @staticmethod
#     def custom_statik_method():
#         print(f'ustom_statik_method')
#
# Myclass.custom_statik_method()

# class Person():
#     @staticmethod
#     def is_adult(age):
#         if age > 18:
#             return True
#         else:
#             return False
# print(Person.is_adult(23))


# class MyClass():
#     TOTAL_OBJECT = 0
#
#     def __init__(self):
#         MyClass.TOTAL_OBJECT = MyClass.TOTAL_OBJECT + 1
#
#     @classmethod
#     def total_object(cls):
#         print(f'Total object', cls.TOTAL_OBJECT)
#
# my_obj = MyClass()
# my_obj_1 = MyClass()
# my_obj_2 = MyClass()

# MyClass.total_object()
#
# class ChildClass(MyClass):
#     TOTAL_OBJECT = 0
#     pass
# print(ChildClass.TOTAL_OBJECT)

# Ȅоздайте класс Human.
# ȁпределите для него два статических поля: default_name и default_age.
# Ȅоздайте метод init(), который помимо self принимает еще два параметра: name и
# age. Для этих параметров задайте значения по умолчанию, используя свойства
# default_name и default_age. В методе init() определите четыре свойства:
# Ȃубличные - name и age. Ȃриватные - money и house.
# ȃеализуйте справочный метод info(), который будет выводить поля name, age, house и
# money.
# ȃеализуйте справочный статический метод default_info(), который будет выводить
# статические поля default_name и default_age.
# ȃеализуйте метод earn_money(), увеличивающий значение свойства money.


# class Human:
#     default_name = 'Dima'
#     default_age = 31
#
#     def __init__(self, name=default_name, age=default_age):
#         self.name = name
#         self.age = age
#         self.__money = 0
#         self.__house = 'House'

    # def info(self):
    #     return (f'name: {self.name}, '
    #             f'age: {self.age}, '
    #             f'money: {self.__money}, '
    #             f'house: {self.__house} ')
    # @staticmethod
    # def default_info():
    #     return (f'name: {Human.default_name}, '
    #             f'age: {Human.default_age}')
    #
    # def earn_money(self, amount):
    #     self.__money += amount
    #     return f'+ {amount} == {self.__money}'

# print(Human.default_info())
# human = Human('Petr',30)
# print(human.info())
# print(human.earn_money(10))
# print(human.earn_money(10))
# print(human.info())

# class Phone:
#     def __init__(self):
#         self.is_on = False
#     def tern_on(self):
#         self.is_on = True
#
#     def call(self):
#         if self.is_on:
#             return f'start calling'
#
# class Mobile(Phone):
#     def __init__(self):
#         super().__init__()
#         self.battery = 0
#
#     def charge(self, per):
#         self.battery = per
#         return f'charging. Now => {self.battery}'
#
# mobile = Mobile()
# print(dir(mobile))
# print(mobile.is_on)
# mobile.tern_on()
# print(mobile.is_on)
#
# class Toy_phone(Phone):
#     def toy_ph(self):
#         print(f'Child Class Toy_ph')
#
# toy_ph = Toy_phone()
# print(toy_ph.is_on)
# toy_ph.toy_ph()


# class Camera:
#     def camera(self):
#         pass
# class Radio:
#     def radio(self):
#         pass
#     def camera(self):
#         pass
#
# class Phone(Camera, Radio):
#     def phone(self):
#         pass
# # #
# print(Phone().__dir__())

# Класс Human
# ȃеализуйте приватный метод
# make_deal(), который будет отвечать
# за техническую реализацию
# покупки дома: уменьшать
# количество денег на счету и
# присваивать ссылку на только что
# купленный дом. В качестве
# аргументов данный метод
# принимает объект дома и его цену.
# ȃеализуйте метод buy_house(),
# который будет проверять, что у
# человека достаточно денег для
# покупки, и совершать сделку. Если
# денег слишком мало - нужно
# вывести предупреждение в
# консоль. Ȃараметры метода: ссылка
# на дом и размер скидки\

# class House:
#     def __init__(self, area, price):
#         self._area = area
#         self._price = price
#
#     def final_price(self, sale):
#         final_sale = self._price - sale
#         return final_sale
#
# class SmallHouse(House):
#     default_area = 40
#     def __init__(self, price):
#         super().__init__(SmallHouse.default_area, price)
#
# small_house = SmallHouse(5)
#
# class Human:
#     def __init__(self, money = 100):
#         self.money = money
#     def __make_deal(house: House, price):
#
#
#
#     def buy_house(house: House, sale):
#         pass




