import asyncio

async def my_coroutine():
    print('my_coroutine')


@asyncio.coroutine
def my_coroutine2():
    print('my_coroutine')

loop = asyncio.get_event_loop()

loop.run_until_complete(my_coroutine())      # blocks until coroutine is complete
loop.run_until_complete(my_coroutine2())
loop.close()
