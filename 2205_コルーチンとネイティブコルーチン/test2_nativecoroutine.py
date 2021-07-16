import asyncio

loop = asyncio.get_event_loop()


async def worker():
    print('start')
    await asyncio.sleep(2)
    print('stop')

if __name__ == '__main__':
    loop.run_until_complete(asyncio.wait([worker(), worker()]))
    loop.close()
