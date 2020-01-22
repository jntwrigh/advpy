"""
    06b_client.py           -           Standard Python APIs can talk to the Twisted
                                        server.  (Start 06_message.py first after installing
                                        Twisted).  This code can be run under Py 2 or Py 3


"""
import socket

sock = socket.socket()

sock.connect(('localhost', 8010))
byte_data = sock.recv(32728)
print(byte_data.decode())
sock.close()
