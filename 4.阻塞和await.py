import asyncio
import time



now = lambda :time.time()

async def do_some_work(x):
    print("waiting:",x)
    # await 后面就是调用耗时的操作
    # （此时do_some_work函数将会挂起，主程序将去执行其他协程，直到其他协程运行完，则返回此函数继续执行）
    await asyncio.sleep(x)
    return "Done after {}s".format(x)


start = now()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
loop.run_until_complete(task)

print("Task ret:", task.result())
print("Time:", now() - start)