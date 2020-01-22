"""

    12_timeout.py       -   In this example, if the count takes
                            longer than 3 seconds to complete, it will
                            timeout and the error message will be seen.
                            The actual function randomly takes between
                            1 and 4 seconds each time so every so often it will
                            timeout.  Run this multiple
                            times and you will see varying results.

"""
import asyncio
import random


async def count(future, name='count1', max_count=10):
    for i in range(max_count):
        print(name, i)
    await asyncio.sleep(random.randint(1, 4))
    if not future.cancelled():
        future.set_result('{0} finished'.format(name))


def finished(future):
    print(future.result())

loop = asyncio.get_event_loop()
future1 = loop.create_future()
future1.add_done_callback(finished)

try:
    loop.run_until_complete(asyncio.wait_for(count(future1), 3))
except asyncio.TimeoutError:
    print('count() took too long before wait_for() timed out.')
finally:
    loop.close()
