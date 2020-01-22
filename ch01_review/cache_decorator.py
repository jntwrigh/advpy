"""

      08_cache_decorator.py    -   Provides a decorator that can
                                   cache the results of calling a
                                   function when similar arguments are
                                   provided

                                   Import and use as a decorator on other
                                   functions.
"""


def cache(orig_func):
    result_cache = {}

    def wrapper(*args, **kwargs):
        if args not in result_cache:			 # it was not in cache
            ret = orig_func(*args, **kwargs)
            result_cache[args] = ret			 # store results in cache
        else:
            print('pinging cache...')
        return result_cache[args]

    return wrapper
