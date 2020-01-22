import asyncio
import logging

logging.basicConfig(level=logging.DEBUG)


def callback(name):
    print('Callback called: {0}'.format(name))


def finished(loop):
    loop.stop()


loop = asyncio.get_event_loop()
loop.set_debug(True)

delay = 4
when = loop.time() + 2

loop.call_later(delay, callback, 'call_later')
loop.call_soon(callback, 'call_soon')
loop.call_soon_threadsafe(callback, 'call_soon_threadsafe')
loop.call_at(when, callback, 'call_at')
loop.call_later(5, finished, loop)
loop.run_forever()
loop.close()
