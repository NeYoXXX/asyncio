import asyncio
import time


now = lambda: time.time()

async def do_some_work(x):
    print("waiting:",x)
    await asyncio.sleep(x)
    return "Done after {}s".format(x)

async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)
    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]
    #第一种 不在main函数中打印结果，直接返回所有的结果集合
    return await asyncio.gather(*tasks)
    #第二种 返回使用asyncio.wait方式挂起协程
    #return await asyncio.wait(tasks)

start = now()

loop = asyncio.get_event_loop()
#results所接受的是main函数返回的结果集
results = loop.run_until_complete(main())
#第二种 接受的返回值也与前几个例子相同
#done,pending = loop.run_until_complete(main())
for result in results:
    print("Task ret:",result)

print("Time:", now()-start)