"""

    13c_executors - This version correctly queues 3 tasks
                    and uses the add_done_callback() technique to get
                    the results after the function completes.  So, whichever function
                    completes first will have their results shown first.

"""

import asyncio
import os
import time
from concurrent.futures import ProcessPoolExecutor

import requests


def get_slow(secs):
    time.sleep(secs)                       # no yield here!
    return 'done'


def get_url(url):
    return requests.get(url).headers


def get_resources(directory):
    return os.listdir(directory)


def show_me(future):
    print(future.result(), flush=True)


def stop_loop():
    loop.stop()


def main():
    with ProcessPoolExecutor() as executor:
        future1 = loop.run_in_executor(executor, get_slow, 5)
        future1.add_done_callback(show_me)
        future2 = loop.run_in_executor(executor, get_url, 'http://www.cisco.com')
        future2.add_done_callback(show_me)
        future3 = loop.run_in_executor(executor, get_resources, '.')
        future3.add_done_callback(show_me)

if __name__ == '__main__':
   loop = asyncio.get_event_loop()
   loop.call_soon(main)
   loop.call_later(6, stop_loop)
   loop.run_forever()
