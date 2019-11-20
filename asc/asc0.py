import asyncio
import time


async def do_something(s):
    print(f'sleep: {s} sec')
    await asyncio.sleep(s)
    result = f'sleep: {s} sec'
    return result


async def save(data):
    await asyncio.sleep(1)
    result = f'date: {data} save done'
    return result


async def indicator():
    result = dict(
        e=await do_something(5),
        a=await do_something(1),
        c=await do_something(3),
        b=await do_something(2),
        d=await do_something(4),
    )

    return result


async def indicator2():
    result = dict(
        e=None,
        a=None,
        c=None,
        b=None,
        d=None,
    )

    coroutine5 = do_something(5),
    coroutine1 = do_something(1),
    coroutine3 = do_something(3),
    coroutine2 = do_something(2),
    coroutine4 = do_something(4),

    tasks = [
        asyncio.ensure_future(coroutine5),
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine3),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine4),
    ]

    # dones, pendings = await asyncio.wait(tasks)
    # for task in dones:
    #     print("Task ret:", task.result())

    results = await asyncio.gather(*tasks)
    for r in results:
        print("Task ret:", r)

    return result


async def calculate(i):
    d = time.time()
    print(f'calculate {i} 次调用')
    data = await indicator()

    result = await save(data)
    e = time.time()
    print(f'calculate {i} 次调用 耗时 {e-d}s')
    return result


async def calculate2(i):
    d = time.time()
    print(f'calculate2 {i} 次调用')
    # data = await indicator2()
    loop_ = asyncio.new_event_loop()
    loop_.run_in_executor(None, func=indicator2)

    # result = await save(data)
    e = time.time()
    print(f'calculate2 {i} 次调用 耗时 {e-d}s')
    # return result


async def run():
    await calculate(1)
    await calculate(2)
    await calculate(3)


async def run2():
    await calculate2(1)
    await calculate2(2)
    await calculate2(3)


async def run3():
    c1 = calculate(1)
    c2 = calculate(2)
    c3 = calculate(3)

    tasks = [
        asyncio.ensure_future(c1),
        asyncio.ensure_future(c2),
        asyncio.ensure_future(c3),
    ]

    results = await asyncio.gather(*tasks)
    for r in results:
        print("Task ret:", r)


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    # loop.run_until_complete(run())
    loop.run_until_complete(run2())









