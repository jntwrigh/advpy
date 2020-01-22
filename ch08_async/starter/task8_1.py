import asyncio
import os
from asyncio import subprocess
from contextlib import closing


# step 1. Make the function an asynchronous coroutine by adding the appropriate
#         keyword before the def keyword below
def ping(future, host, loop=None, number=2):

    if not loop:
        loop = asyncio.get_event_loop()

    # step 2.  use the create_subprocess_exec() function to
    #          perform a ping call.  Pipe the stdout back.
    #          Be sure to invoke create_subprocess_exec() following an 'await' statement
    #
    #          Also add a proc.communicate() call, also with an 'await'
    #          in front of it.


    # step 3.  use the stdout result from the above call in step 2 to
    #          set the result of the future that was passed in.
    #          (when the set_result() is called, this will invoke any
    #          callbacks on the future that were set).



# step 4. create a function that will be invoked once the future is finished
#         (e.g. the result is set in the ping method).
#         This function is simple: it passes in a future, then prints
#         its result.


def get_loop():
    """
        returns either the std asyncio loop for all os's or the ProactorEventLoop for Windows.
    """
    loop = asyncio.get_event_loop()
    if os.name == 'nt':
        loop = asyncio.ProactorEventLoop()
        asyncio.set_event_loop(loop)

    return loop


with closing(get_loop()) as loop:
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

    # step 5. iterate over the hosts list above.  For each host do
    #         the following:
    #           1) create a Future object using loop.create_future()
    #           2) invoke its add_done_callback() passing a reference to
    #              the callback function created in step 4
    #           3) create (and enqueue) a task using asyncio.ensure_future()
    #              providing the call to the ping method.  Pass into the
    #              future, the host, and the loop.
    #           4) append this task to a list of tasks
    #           5) end the for-loop.
    #
    #         After the for-loop, invoke the loop's run_until_complete()
    #         method passing:   asyncio.wait(tasks)


