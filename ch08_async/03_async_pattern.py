"""
    03_async_pattern.py     -   this example is not meant to be run, but could be.
                                It assumes there is a server running at each of the
                                ports listed at the bottom.  Therefore if you create
                                simple servers (we've done this in previous courses)
                                you can perform this example.
"""

import errno
import select
import socket


def retrieve_data(sockets):
    while sockets:
        sockets_ready, _, _ = select.select(sockets, [], [])

        for sock in sockets_ready:
            data = ''
            while True:
                try:
                    data_in = sock.recv(1024)
                except socket.error as e:
                    if e.args[0] == errno.EWOULDBLOCK:
                        break
                    raise
                else:
                    if not data_in:
                        break
                    else:
                        data += data_in

            if not data:
                sockets.remove(sock)
                sock.close()
                print('Socket Finished')

            data_dict[sock] += data


def create_sockets(addresses):
    sockets = []
    for address in addresses:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(address)
        sock.setblocking(False)
        sockets.append(sock)
    return sockets


data_dict = {}
addresses = [('localhost', 8010), ('localhost', 8011), ('localhost', 8012)]
sockets = create_sockets(addresses)
retrieve_data(sockets)
