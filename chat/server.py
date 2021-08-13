import asyncio

writers = []

def forward(writer, addr, message):
    for w in writers:
        if w != writer:
            w.write(f'{addr}: {message}\n'.encode())


async def handle(reader, writer):
    writers.append(writer)
    addr = writer.get_extra_info('peername')
    message = f'{addr} is connected!'
    print(message)
    forward(writer, addr, message)

    while True:
        data = await reader.read(1024)
        message = data.decode().strip()
        forward(writer, addr, message)
        await writer.drain()

        if message == 'bye':
            message = f'{addr} wants to close the connection'
            print(message)
            forward(writer, 'Server', message)
            break

    writers.remove(writer)
    writer.close()


async def main():
    server = await asyncio.start_server(handle, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')
    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())
