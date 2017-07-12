import asyncio

async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print('Received {} from {}'.format(message, addr))

    print('Send: {}'.format(message))
    writer.write(data)
    await writer.drain()

    print('Close the client socket')
    writer.close()

loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, '127.0.0.1', 10000, loop=loop)
try:
    server = loop.run_until_complete(coro)
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
