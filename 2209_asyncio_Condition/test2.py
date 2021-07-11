######
# conditionは、Lockと同じように動く
# 以下ではworker3が終わったあと、worker1か2のどちらかがlockをとって動きます
######
import asyncio


loop = asyncio.get_event_loop()


async def worker1(condition):
    async with condition:
        condition.wait()
        print('worker1 start')
        print('worker1 got condition')
        await asyncio.sleep(3)
        print('worker1 end')


async def worker2(condition):
    async with condition:
        condition.wait()
        print('worker2 start')
        print('worker2 got condition')
        await asyncio.sleep(3)
        print('worker2 end')


async def worker3(condition):
    async with condition:
        print('worker3 start')
        await asyncio.sleep(3)
        print('worker3 end')
        condition.notify_all()

condition = asyncio.Condition()
loop.run_until_complete(asyncio.wait([
    worker1(condition), worker2(condition), worker3(condition)
]))
loop.close()
