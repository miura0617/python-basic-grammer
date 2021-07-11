import asyncio


loop = asyncio.get_event_loop()


async def worker1(queue):
    print('asyncio native start1')
    await queue.put(100)
    print('asyncio native stop1')


async def worker2(queue):
    print('asyncio native start2')
    x = await queue.get()
    print(x)
    print('asyncio native stop2')


if __name__ == '__main__':
    queue = asyncio.Queue()
    loop.run_until_complete(asyncio.wait([
        worker1(queue), worker2(queue)
    ]))
    loop.close()
