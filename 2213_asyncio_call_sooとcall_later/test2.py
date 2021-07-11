######################################################
# スケジューリング 例）何秒後にタスクを動かすなど
######################################################
import asyncio


loop = asyncio.get_event_loop()


def hello(name, loop):
    print('Hello {}'.format(name))
    loop.stop()

loop.call_later(3, hello, 'Mike', loop) # 3秒後にhelloタスクを呼び出せる
loop.call_soon(hello, 'Nancy', loop)

loop.run_forever()
loop.close()
