import asyncio
import time


async def get_application():
    print('get_application start')
    await asyncio.sleep(2)
    # result = {'application_id': 123}
    result = 123
    print('get_application end ,use 2s')
    return result


async def get_member():
    print('get_member start')
    await asyncio.sleep(1)
    # result = {'member_id': 12}
    result = 12
    print('get_member end ,use 1s')
    return result


async def get_basis():
    print('get_basis start')
    await asyncio.sleep(3)
    # result = {'basis_id': 1234}
    result = 1234
    print('get_basis end ,use 3s')
    return result


async def save(data):
    result = {}
    await asyncio.sleep(0.5)
    result.update(data)
    print(f'date: {data} save done')
    return result


async def get_data():
    application = get_application()
    basis = get_basis()
    member = get_member()

    tasks = [
        asyncio.ensure_future(basis),
        asyncio.ensure_future(member),
        asyncio.ensure_future(application),
    ]
    return await asyncio.gather(*tasks)


def creat_date():
    loop_ = asyncio.new_event_loop()
    results = loop_.run_until_complete(get_data())
    loop_.close()
    return results


async def indicator():
    col_list = ['basis', 'member', 'application']
    data = {}
    result_dict = await loop.run_in_executor(None, creat_date)
    for d in range(len(col_list)):
        data.update({col_list[d]: result_dict[d]})
    return data


async def calculate(i):
    d = time.time()
    print(f'calculate {i} 次调用')
    result = await indicator()

    e = time.time()
    print(f'calculate {i} 次调用 耗时 {e-d}s')
    print(result)
    return result


async def run():
    await calculate(1)
    await calculate(2)
    await calculate(3)


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())









