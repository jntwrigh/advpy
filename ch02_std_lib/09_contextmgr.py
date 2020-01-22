"""

    09_contextmgr.py     -  This example retrieves the HTML from 16 websites, parses each one
                            and returns the HTML title of each page.  It does this using
                            10 threads.

                            The ThreadPool class is a context manager that instantiates the pool
                            of threads.  The enter method starts the threads.  The with control is
                            used with the ThreadPool class to queue up a bunch of jobs into the req_queue.
                            The exit method adds sentinel values to the request queue.

                            Both the ThreadPool class and the WorkerThread class are written generically,
                            so they should work with any function that supplies arguments and returns a value.
                            The arguments can be pulled off of the request queue.  The function each thread calls
                            can be provided from the WorkerThread class constructor.

                            To try your own solution, replace get_data() with a different function and then
                            queue up your own arguments.
"""

import requests
from bs4 import BeautifulSoup

from ch02_std_lib.worker_thread import ThreadPool


def get_data(url):
    """
        This is the work we are trying to perform (provides a URL, fetches HTML, returns the page's title)
    """
    try:
        text = requests.get(url).text
        soup = BeautifulSoup(text, 'html.parser')
        result = soup.title.text
    except (TypeError, requests.exceptions.ConnectionError) as err:
        result = err.args[0]

    return result


tasks = ['http://python-requests.org', 'https://www.google.com', 'https://pypi.python.org',
         'https://www.cisco.com', 'http://www.python.org', 'http://love-python.blogspot.com/',
         'http://planetpython.org', 'https://www.python.org/doc/humor/', 'http://lucumr.pocoo.org/',
         'https://doughellmann.com/blog/', 'https://pymotw.com/3/', 'http://python-history.blogspot.com/',
         'https://nothingbutsnark.svbtle.com/','https://www.pydanny.com/','https://pythontips.com/',
         'http://www.blog.pythonlibrary.org/']

pool = ThreadPool(get_data)             # set logging_on=True in constructor to see detailed output

with pool as req_queue:
    for url in tasks:
        req_queue.put((url,))

print('Results:')
for result in pool.get_results():
    print(result)


# uncomment the code below to try a different function
# def calc_area(w, h):
#     return w*h

# areas = [(10, 10), (5, 1), (15, 25), (10, 0)]
# pool = ThreadPool(calc_area, num_threads=20, logging_on=True)
# with pool as req_queue:
#     for area in areas:
#         req_queue.put(area)
# print('Results:')
# for result in pool.get_results():
#     print(result)
