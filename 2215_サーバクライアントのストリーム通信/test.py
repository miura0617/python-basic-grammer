import asyncio


loop = asyncio.get_event_loop()


async def main():
    print('start')
    await asyncio.sleep(3)      # ここのIOバウンドを、次からネットワーク通信にして勉強していく
    print('done')

loop.run_until_complete(main())
loop.close()
