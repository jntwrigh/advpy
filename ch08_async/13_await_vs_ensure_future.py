"""
            13_async_vs_yield.py        -   This example runs two main
                                            functions (main & main2) that
                                            queue up the my_coroutine1 and
                                            my_coroutine2 in different ways.
                                            To identify this difference, we
                                            make main take 4 seconds,
                                            my_coroutine1 take 1 second,
                                            and my_coroutine2 take 2 seconds

                                            The results are that main1 takes
                                            7 seconds: mycoroutine1 + mycoroutine2 + main

                                            main2 takes 4 seconds.
"""
import asyncio


async def task1():
    await asyncio.sleep(1)
    print('task1')


async def task2():
    await asyncio.sleep(2)
    print('task2')


async def main():
    await task1()
    await task2()
    await asyncio.sleep(4)


loop = asyncio.get_event_loop()
start = loop.time()
loop.run_until_complete(main())
finish = loop.time()
print('Total time elapsed: {0}'.format(finish - start))


async def main2():
    asyncio.ensure_future(task1())
    asyncio.ensure_future(task2())
    await asyncio.sleep(4)


loop = asyncio.get_event_loop()
start = loop.time()
loop.run_until_complete(main2())
finish = loop.time()
print('Total time elapsed: {0}'.format(finish - start))
loop.close()
