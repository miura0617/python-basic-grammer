# asyncioのStreams
# https://docs.python.org/ja/3.6/library/asyncio-stream.html
import asyncio


loop = asyncio.get_event_loop()

class AwaitableClass(object):
    def __init__(self, name, loop):
        self.name = name
        self.loop = loop
 
    # 特殊メソッド内でawait使えないので、古い書き方のyeild fromを使う
    # 特殊メソッドを使って、非同期処理も書ける
    def __await__(self):
        @asyncio.coroutine
        def wrapper():
            reader, writer = yield from asyncio.open_connection(
                '127.0.0.1', 8888, loop=self.loop)
            writer.write(self.name.encode())
            writer.write_eof()
            data = yield from reader.read()
            data = int(data.decode())
            return data
        return (yield from wrapper())

class AsyncIterater(object):
    def __init__(self, name, loop):
        self.name = name
        self.loop = loop
    
    def __aiter__(self):
        return self

    async def __anext__(self):
        data = await AwaitableClass(self.name, self.loop)
        if data < 0:
            raise StopAsyncIteration
        return data

async def main(name, loop):
    print('chunk reader')
    # result = await AwaitableClass(name, loop)
    async for i in AsyncIterater(name, loop):
        print(i)

loop.run_until_complete(asyncio.wait([
    main('task1', loop), main('task2', loop)]))
loop.close()
