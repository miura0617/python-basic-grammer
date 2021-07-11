######################################################
# タスクを実行した結果を受け取るときにFutureを使う
######################################################
import asyncio


loop = asyncio.get_event_loop()


async def f(future):
    await asyncio.sleep(1)
    future.set_result('Future is done!')

# コールバックもできる
def got_result(future):
    print(future.result())
    loop.stop()

future = asyncio.Future()
asyncio.ensure_future(f(future))

future.add_done_callback(got_result)

loop.run_forever()  # コールバックgot_result()内でloop.stop()されて、次の処理へ
loop.close()
