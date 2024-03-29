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
    #使用as_completed函数返回
    for task in asyncio.as_completed(tasks):
        result = await task
        print("Task ret: {}".format(result))

start = now()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print("Time:", now()-start)