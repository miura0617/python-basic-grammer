"""
REST

HTTPメソッド　クライアントが行いたい処理をサーバに伝える

GET        データの参照
POST       データの新規登録
PUT        データの更新
DELETE     データの削除
"""

import urllib.request
import json


# URLにパラメータを渡したい場合
payload = {'key1': 'value1', 'key2': 'value2'}



url = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
print(url)

with urllib.request.urlopen(url) as f:
    #print(f.read().decode('utf-8'))   # json形式で返ってくる
    r = json.loads(f.read().decode('utf-8'))
    print(r)
    print(type(r))
