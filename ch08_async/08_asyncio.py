import asyncio


def task():
    print('Running task')
    loop.stop()

loop = asyncio.get_event_loop()

loop.call_soon(task)

print('Event loop starting...')
loop.run_forever()
loop.close()
