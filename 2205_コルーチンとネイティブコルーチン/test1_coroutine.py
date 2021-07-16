import asyncio

loop = asyncio.get_event_loop()

@asyncio.coroutine
def worker():
    print('start')
    yield from asyncio.sleep(2)
    print('stop')

if __name__ == '__main__':
    loop.run_until_complete(asyncio.wait([worker(), worker()]))
    loop.close()
