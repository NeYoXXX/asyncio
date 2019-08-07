import time
import asyncio


now = lambda : time.time()


async def do_some_work(x):
    print("waiting:",x)
    return "Done after {}s".format(x)


def callback(future):
    #回调函数有future类的参数
    print("callback:",future.result())


start = now()
coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
print(task)
#增加回调函数
task.add_done_callback(callback) 
print(task)
loop.run_until_complete(task)

print("Time:", now()-start)