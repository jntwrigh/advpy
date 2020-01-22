"""
        11b_await.py

        First, await has become yield from in Python 3.5+.  If you are using Py 3.5,
        you may replace yield from with await below and no change will occur.

        Also, the @async.coroutine may be replaced with the async def keyword on the
        function definition in Python 3.5.

        Second, await causes the current task's execution to be paused so that the event
        loop may go off and handle the specified subtask.  The currently executing
        coroutine will not continue until the coroutine that follows await is finished.

        Use of asyncio.sleep() simply causes the task
        to wait until the sleep period is over, but the asyncio version will return to
        the event loop to process other tasks in the mean time.
"""
import asyncio


async def count(number, version):
    for i in range(number):
        print('{0}: {1}'.format(version, i))
        # await asyncio.sleep(0)                            # run this then, uncomment and run it again

loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(count(3, 't1')),                  # ensure_future simply wraps a coroutine in a future to ensure it is a future object
    asyncio.ensure_future(count(5, 't2')),
    asyncio.ensure_future(count(7, 't3')),
]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()
