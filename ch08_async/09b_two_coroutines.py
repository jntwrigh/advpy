"""
    09b_two_coroutines.py   - runs the event loop forever, adds two coroutines into the
                              loop.  Loop is shut down after 10 seconds.
"""
import asyncio
from datetime import datetime


async def shutdown_loop():
    if loop.is_running():
        loop.stop()

async def show_time(id, loop):
    while True:
        print('{0}, loop {1}'.format(datetime.now().strftime('%b %d (%H:%M:%S)'), id))
        if (loop.time() + 1.0) >= end_time:
            await shutdown_loop()
        await asyncio.sleep(2)


loop = asyncio.get_event_loop()
end_time = loop.time() + 10.0
asyncio.ensure_future(show_time(id=1, loop=loop))
asyncio.ensure_future(show_time(id=2, loop=loop))

loop.run_forever()
