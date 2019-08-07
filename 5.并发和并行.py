import asyncio
import time


now = lambda :time.time()


async def do_some_work(x):
    print("Waiting:",x)
    await asyncio.sleep(x)
    print("finish:",x)
    return "Done after {}s".format(x)

start = now()

coroutine1 = do_some_work(4)
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(1)

tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3)
]

loop = asyncio.get_event_loop()
#asyncio.wait(tasks) 也可以使用 asyncio.gather(*tasks) ,前者接受一个task列表，后者接收一堆task。
#官网说明
#https://docs.python.org/3/library/asyncio-task.html#asyncio.gather
#https://docs.python.org/3/library/asyncio-task.html#asyncio.wait
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print("Task ret:",task.result())

print("Time:",now()-start)


'''
执行结果：
Waiting: 4
Waiting: 2
Waiting: 1
finish: 1
finish: 2
finish: 4
Task ret: Done after 4s
Task ret: Done after 2s
Task ret: Done after 1s
Time: 4.004289865493774
'''