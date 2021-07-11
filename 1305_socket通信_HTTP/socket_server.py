"""
ウェルノウンポート番号(0 - 1023)
登録済みポート番号(1024 - 49151)
動的・プライベートポート番号(49152 - 65535)
"""

import socket


# AF_INETはIPv4、SOCK_STREAMはTCP/IPの場合使う
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 50007))
    s.listen(1)  # 1つの接続の意味
    while True:
        # コネクションするまで待ち、誰か接続してきたら、connとaddrに情報を入れる
        conn, addr = s.accept()
        # コネクションが終わったら
        with conn:
            while True:
                data = conn.recv(1024)  # 1024個のチャンクを受け取る
                if not data:
                    break
                print(data)
                for i in addr:
                    print(i)
                # dataを受信したら、何かsendで返す
                conn.sendall(b'Received: ' + data)

