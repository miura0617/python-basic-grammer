# asyncioのStreams
# https://docs.python.org/ja/3.6/library/asyncio-stream.html
import asyncio

@asyncio.coroutine
def tcp_echo_client(message, loop):
    reader, writer = yield from asyncio.open_connection('127.0.0.1', 8888,
                                                        loop=loop)

    print('Send: %r' % message)
    writer.write(message.encode())

    data = yield from reader.read(100)
    print('Received: %r' % data.decode())

    print('Close the socket')
    writer.close()

message = 'Hello World!'
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([
    tcp_echo_client(message, loop),
    tcp_echo_client(message, loop),
    tcp_echo_client(message, loop),
    tcp_echo_client(message, loop)]))
loop.close()