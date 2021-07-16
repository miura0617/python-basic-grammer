######################################################
# タスクとコルーチン
# https://docs.python.org/ja/3.6/library/asyncio-task.html
######################################################
import asyncio

async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(3.0)            # この1秒間の間に、別タスクを実行できる
    return x + y

async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([print_sum(1, 2), print_sum(3, 2)]))
loop.close()
