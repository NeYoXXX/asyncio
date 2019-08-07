import asyncio
import time


now = lambda: time.time()


async def do_some_work(x):
    print("waiting:", x)

start = now()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
#创建一个task对象，与coroutine对象没有本质的区别，在coroutine对象的基础上进行封装
#创建task对象有两种方式，第一种是loop.create_task，第二种是asyncio.ensure_future
#（task对象是Future类的子类，保存了协程运行后的状态，用于未来获取协程的结果）
#官方文档 
# https://docs.python.org/3/library/asyncio-task.html#asyncio.ensure_future
# https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.AbstractEventLoop.create_task
task = loop.create_task(coroutine)  
print(task)
loop.run_until_complete(task)
print(task)
print("Time:",now()-start)