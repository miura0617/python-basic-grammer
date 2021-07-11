######################################################
# タスクを実行した結果を受け取るときにFutureを使う
######################################################
import asyncio


loop = asyncio.get_event_loop()


async def f(future):
    await asyncio.sleep(1)
    future.set_result('Future is done!')


future = asyncio.Future()
asyncio.ensure_future(f(future))
loop.run_until_complete(future)  # 引数が関数fではなく、futureであることに注意
print(future.result())
loop.close()
