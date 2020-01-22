from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol
from sys import stdout


class Message(Protocol):
    def dataReceived(self, msg):
        stdout.write(msg)
        delayed_call = 1
        reactor.callLater(delayed_call, shutdown)


def shutdown():
    reactor.stop()

endpoint = TCP4ClientEndpoint(reactor, "localhost", 8010)
protocol = Message()
connectProtocol(endpoint, protocol)

reactor.run()
