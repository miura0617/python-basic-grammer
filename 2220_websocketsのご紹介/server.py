# websockets
# https://websockets.readthedocs.io/en/stable/intro.html
# 【確認方法】
# 「python server.py」を実行
# index.htmlをブラウザで開き、時間がどんどん表示されることを確認する
# index.htmlのURLを複数ページ開き、複数ページに時間が非同期で表示されることを確認する
import asyncio
import datetime
import random
import websockets

async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
