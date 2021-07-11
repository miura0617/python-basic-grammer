import asyncio


loop = asyncio.get_event_loop()


async def worker1(semaphore):
    async with semaphore:
        print('asyncio native start1')
        await asyncio.sleep(3)
        print('asyncio native stop1')


async def worker2(semaphore):
    async with semaphore:
        print('asyncio native start2')
        await asyncio.sleep(3)
        print('asyncio native stop2')


if __name__ == '__main__':
    semaphore = asyncio.Semaphore(2)
    loop.run_until_complete(asyncio.wait([
        worker1(semaphore), worker2(semaphore)
    ]))
    loop.close()
