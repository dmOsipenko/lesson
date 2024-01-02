import time
import asyncio
import requests
from aiohttp import ClientSession

# def func_1(x):
#     print(f'start func_1...')
#     print(f'x ** 2 = {x ** 2}')
#     print(f'func_1 sleeping...')
#     time.sleep(3)
#     print(f'func_1 get up and finishing....')
#
#
# def func_2(x):
#     print(f'start func_2...')
#     print(f'x ** 2 = {x ** 0.5}')
#     print(f'func_2 sleeping...')
#     time.sleep(3)
#     print(f'func_2 get up and finishing....')


# async def func_1(x):
#     print(f'x ** 2 = {x ** 2}')
#     await asyncio.sleep(3)
#     print(f'func_1 finish....')
#
#
# async def func_2(x):
#     print(f'x ** 2 = {x ** 0.5}')
#     await asyncio.sleep(3)
#     print(f'func_2 finish....')
#
#
# async def main():
#     task_1 = asyncio.create_task(func_1(4))
#     task_2 = asyncio.create_task(func_2(4))
#
#     await asyncio.gather(task_1,task_2)
#
#
# print(time.strftime('%X'), ': start program')
# asyncio.run(main())
# print(time.strftime('%X'), ': finish program')

# print(type(func_1))
# print(type(func_1(4))) #КОРУТИНА

# Тоже самое, только немного другое написание кода

# async def func_1(x):
#     print(f'x ** 2 = {x ** 2}')
#     await asyncio.sleep(3)
#     print(f'func_1 finish....')
#
#
# async def func_2(x):
#     print(f'x ** 2 = {x ** 0.5}')
#     await asyncio.sleep(3)
#     print(f'func_2 finish....')
#
#
# print(time.strftime('%X'))
#
# loop = asyncio.get_event_loop()
# task_1 = loop.create_task(func_1(4))
# task_2 = loop.create_task(func_2(4))
# loop.run_until_complete(asyncio.wait([task_1,task_2]))
#
#
# print(time.strftime('%X'))


# async def get_con(host, port):
#     class Con:
#         async def put_data(self):
#             print('send some data...')
#             await asyncio.sleep(2)
#             print('data send')
#     #
#         async def get_data(self):
#             print('get some data...')
#             await asyncio.sleep(2)
#             print('get data')
#     #
#         async def close(self):
#             print('close connection...')
#             await asyncio.sleep(2)
#             print('connection is close')
#     #
#     print('conection...')
#     await asyncio.sleep(2)
#     print('connect')
#     return Con()
#
#
# asyncio.run(get_con(1, 2))


#
#ASYNC
# async def get_async_weather(my_city):
#     async with ClientSession() as session:
#         url = 'https://openweathermap.org/data/2.5/find'
#         params = {'q': my_city, 'appid': '439d4b804bc8187953eb36d2a8c26a02'}
#         async with session.get(url, params=params) as responce:
#             weather_data = await responce.json()
#             print(f'{my_city}:{weather_data["list"]}')
#
#
# async def main(cities):
#     tasks = []
#     for city in cities:
#         tasks.append(asyncio.create_task(get_async_weather(city)))
#
#     for task in tasks:
#         await task
#
#
# print(time.strftime('%X'))
# cities = ['Minsk', 'Paris']
# asyncio.run(main(cities))
# print(time.strftime('%X'))


def get_sync_weather(my_city):
    url = 'https://openweathermap.org/data/2.5/find'
    params = {'q': my_city, 'appid': '439d4b804bc8187953eb36d2a8c26a02'}
    rec = requests.get(url=url,params=params)
    weather_data = rec.json()
    print(f'{my_city}:{weather_data["list"]}')

def main(cities):
    for city in cities:
        get_sync_weather(city)


print(time.strftime('%X'))
cities = ['Minsk', 'Paris', 'Brest', 'Moscow']
main(cities)
print(time.strftime('%X'))