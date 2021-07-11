#   ベースサンプル：https://zeromq.org/languages/python/
#   
#   PUBとSUBは、リアルタイムでサーバからデータをとってきたい場合に使う

import zmq


context = zmq.Context()
sock = context.socket(zmq.SUB)
sock.setsockopt(zmq.SUBSCRIBE, b'sub1:')  # 第二引数はフィルタ
sock.connect("tcp://127.0.0.1:5690")

while True:
    message = sock.recv()
    print("Received: {}".format(message.decode()))
