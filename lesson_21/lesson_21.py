import asyncio
import multiprocessing
import time
import threading
from threading import Thread,Lock
import random
from aiohttp import ClientSession


# async def async_func():
#     print(f'start...')
#     await asyncio.sleep(1)
#     print(f'...finish')
#
# async def head_func():
#     await async_func()
#
# asyncio.run(head_func())


# async def async_func(tast):
#     print(f'{tast} start...')
#     await asyncio.sleep(1)
#     print(f'{tast} ...finish')
#
#
# async def head_func():
#     task_a = loop.create_task(async_func('task_a'))
#     task_b = loop.create_task(async_func('task_b'))
#     task_c = loop.create_task(async_func('task_c'))
#     await asyncio.wait([task_a, task_b, task_c])
#
#
# if __name__ == "__main__":
#     try:
#         loop = asyncio.get_event_loop()
#         loop.run_until_complete(head_func())
#     except:
#         pass
#
# asyncio.run(head_func())

#
# async def fetch_url_data(session, url):
#     try:
#         async with session.get(url, timeout=60) as response:
#             resp = await response.read()
#     except Exception as e:
#         print(e)
#     else:
#         return resp
#     return
#
#
# async def featch_async(loop, r):
#     url = 'https://www.uefa.com/uefaeuro-2020/'
#     tasks = []
#     async with ClientSession() as session:
#         for i in range(r):
#             task = asyncio.ensure_future(fetch_url_data(session, url))
#             tasks.append(task)
#         resp = await asyncio.gather(*tasks)
#     return resp
#
#
# if __name__ == '__main__':
#     for count in [1, 10, 100, 1000]:
#         start_time = time.time()
#         loop = asyncio.get_event_loop()
#         future = asyncio.ensure_future(featch_async(loop,count))
#         loop.run_until_complete(future)
#         responses = future.result()
#         print(f'у нас есть {count} результатов за {time.time() - start_time} сек')


# def worker(num):
#     sleep = random.randrange(1, 10)
#     time.sleep(sleep)
#     print(f'I am worker {num}, i am sleeping {sleep} sec')
#
#
# for item in range(3):
#     tr = threading.Thread(target=worker, args=(item,))
#     tr.start()
#
#
# print(f'***finish***')

# class My_Custom_Thread(Thread):
#
#     def __init__(self,num):
#         Thread.__init__(self)
#         self.num = num
#
#     def run(self):
#         for i in range(self.num):
#             print(f'поток My_Custom_Thread #{i}')
#             time.sleep(1)
#
#
# m_c_t = My_Custom_Thread(3)
# m_c_t.run()


lock = Lock()
stop_thread = False

# def my_worker():
#     print(f'start my worker')
#     while True:
#         print('THREAD IS WORK')
#         lock.acquire()
#         if stop_thread is True:
#             break
#         lock.release()
#         time.sleep(1)
#     print(f'finish my worker()')
#
#
# th = Thread(target=my_worker)
# th.start()
# time.sleep(2)
# lock.acquire()
# stop_thread = True
# lock.release()


# def func():
#     for i in range(5):
#         print(f'hello with child thred {i} ')
#         time.sleep(1)
#
#
# th = Thread(target=func)
# th.start()
# print(f'ALL STOP')

# def func():
#     for i in range(5):
#         print(f'hello with child thred {i} ')
#         time.sleep(1)
#
#
# th = Thread(target=func, daemon=True)
# th.start()
# print(f'ALL STOP')


from multiprocessing import Process

# def disp():
#     print(f'Hello!!! Welcom to Python tutorial')
#     if __name__ == 'main':
#         p = Process(target=disp)
#         p.start()
#         p.join()


def cube(n):
    print(f'cube = {n*n*n}')

def square(n):
    print(f'square = {n*n}')

if __name__ == '__main__':
    process_1 = Process(target=cube, args=(2,))
    process_2 = Process(target=square, args=(3,))


    process_1.start()
    process_2.start()


    process_1.join()
    process_2.join()
print(f'ALL FINISH')








