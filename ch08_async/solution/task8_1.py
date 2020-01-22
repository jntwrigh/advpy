import asyncio
import contextlib
import os
import platform


async def ping(future, host, loop=None, number=2):

    if not loop:
        loop = asyncio.get_event_loop()

    cmd = ['ping', '-c', str(number), host]
    if platform.system() == 'Windows':              # change command slightly for Windows OS
        cmd[1] = '-n'

    proc = await asyncio.create_subprocess_exec(*cmd,
                                                stdout=asyncio.subprocess.PIPE,
                                                stderr=asyncio.subprocess.STDOUT,
                                                loop=loop)

    stdout, stderr = await proc.communicate()
    future.set_result(stdout.decode())


def ping_finished(future):
    print(future.result())


def get_loop():
    loop = asyncio.get_event_loop()
    if os.name == 'nt':
        loop = asyncio.ProactorEventLoop()
        asyncio.set_event_loop(loop)

    return loop


with contextlib.closing(get_loop()) as loop:
    tasks = []
    hosts = [
        'www.google.com', 'www.yahoo.com', 'www.cisco.com',
        'www.yelp.com', 'www.im_not_real.com', 'www.espn.com',
        'www.walmart.com', 'www.twitter.com', 'www.facebook.com',
        'www.youtube.com', 'www.wikipedia.org', 'www.go.com',
        'www.ebay.com', 'www.weather.com', 'www.bing.com',
        'www.craigslist.org', 'www.reddit.com', 'www.pinterest.com',
        'www.linkedin.com', 'www.huffingtonpost.com', 'www.apple.com',
        'www.cnn.com', 'www.nytimes.com', 'www.blogspot.com',
        'www.microsoft.com'
    ]

    for host in hosts:
        future = loop.create_future()
        future.add_done_callback(ping_finished)
        task = asyncio.async(ping(future, host, loop))
        tasks.append(task)

    loop.run_until_complete(asyncio.wait(tasks))

