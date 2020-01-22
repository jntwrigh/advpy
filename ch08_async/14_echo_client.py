import asyncio


class EchoClient(asyncio.Protocol):
    message = 'Message to send'

    def connection_made(self, transport):
        transport.write(self.message.encode())
        print('data sent: {0}'.format(self.message))

    def data_received(self, data):
        print('From the server: {0}'.format(data.decode()))

    def connection_lost(self, exc):
        print('connection closed by server')
        asyncio.get_event_loop().stop()

loop = asyncio.get_event_loop()
future = loop.create_connection(EchoClient, '127.0.0.1', 8010)
loop.run_until_complete(future)
loop.run_forever()
loop.close()
