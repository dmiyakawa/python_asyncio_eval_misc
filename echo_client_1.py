import asyncio

async def tcp_echo_client(message, loop):
    reader, writer = await asyncio.open_connection('127.0.0.1', 10000,
                                                   loop=loop)
    print('Send: {}'.format(message))
    writer.write(message.encode())

    data = await reader.read(100)
    print('Received: {}'.format(data.decode()))

    print('Close the socket')
    writer.close()

message = 'Hello World!'
loop = asyncio.get_event_loop()
loop.run_until_complete(tcp_echo_client(message, loop))
loop.close()
