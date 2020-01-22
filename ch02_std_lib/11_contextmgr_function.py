"""
    11_contextmgr_function.py   -   provides an elapsed time for execution of
                                    contents of a with control
"""

import contextlib
import time


@contextlib.contextmanager
def elapsed(name=None):
    timer_name = name
    begin = time.time()
    try:
        yield timer_name
    except Exception as err:
        print(err)
    finally:
        end = time.time()
        print('elapsed time: {0:.3f} seconds'.format(end - begin))


with elapsed():
    entries = open('../resources/access_.log').read()
    # raise Exception('An error occurred.')

with elapsed('first') as a, elapsed('second') as b:
    entries2 = open('../resources/access_.log').read()
    print(a, b)
