import asyncio
import random


# @asyncio.coroutine                    # Python 3.4 uses this syntax instead of async def
async def my_coroutine(task, sleep_time=3):
    print('{0} sleeps {1} seconds'.format(task, sleep_time))
    await asyncio.sleep(sleep_time)     # Python 3.4 uses yield from
    print('{0} is finished'.format(task))


loop = asyncio.get_event_loop()
tasks = [
    my_coroutine('task1', random.randint(1, 4)),
    my_coroutine('task2', random.randint(1, 4)),
    my_coroutine('task3', random.randint(1, 4))
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
