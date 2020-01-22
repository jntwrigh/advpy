import asyncio


class EchoServer(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        print('Connection made')

    def data_received(self, data):
        response = 'Server says: {0} send back'.format(data.decode())
        future = asyncio.async(self.send_response(response))
        print(response)
        try:
            result = asyncio.wait_for(future, 30)
        except TimeoutError:
            result = 'Server failed to respond'
        # could also do yield from self.response(response)
        self.transport.close()

    @asyncio.coroutine
    def send_response(self, response):
        self.transport.write(response.encode())

    def connection_lost(self, exc=''):
        #server.close()    # comment this back in to have server end after one run
        print('Connection closed')

loop = asyncio.get_event_loop()
future = loop.create_server(EchoServer, '127.0.0.1', 8010)
server = loop.run_until_complete(future)
loop.run_until_complete(server.wait_closed())
