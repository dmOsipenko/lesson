# d = {}
# d_1 = {'one':1000}
# print(type(d),d)
# print(type(d_1),d_1)

# d_2 = dict(shot='dict', long='dictionary')
# d_3 = dict([(1,'1'), (2,'2')])
# print(type(d_2),d_2)
# print(type(d_3),d_3)

# d_5 = dict.fromkeys(['a','b','c'], 100)
# print(d_5)
#
# d_6 = dict.fromkeys(['a','b','c'], [100,200,300])
# print(d_6)

# d_10 = {a: a+1 for a in range(10)}

# d_2 = dict(short='dict', long='dictionary')
# print(d_2.get('long'))
# print(d_2.get('key','default')) # если ключа key нет, то покажет другое значение default
# print(d_2.items())
# print(d_2.keys())
# print(d_2.values())
# print(d_2.pop('short'))
# print(d_2)
# print(d_2.popitem()) # удаляет последнее ключ значение
# print(d_2)

# person = {
#     'name':'Dima',
#     'age': 30,
#     'city':'Minsk'
# }
# print(person.get('age'))

cars = {'bmw':[3,5,7],
        'tesla':['model3','modelS','teslaNew']
        }
print(cars['bmw'][0],cars['bmw'][2])
print(cars['tesla'][0],cars['tesla'][2])