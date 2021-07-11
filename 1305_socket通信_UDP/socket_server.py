"""
ウェルノウンポート番号(0 - 1023)
登録済みポート番号(1024 - 49151)
動的・プライベートポート番号(49152 - 65535)
"""

import socket


# AF_INETはIPv4、SOCK_STREAMはTCP/IPの場合使う
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('127.0.0.1', 50007))
    while True:
        data, addr = s.recvfrom(1024)  # 1024個のチャンクを受け取る
        print(data)
        for i in addr:
            print(i)

