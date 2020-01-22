"""

    08_using_cache.py       -       This driver imports the find_airport
                                    function, decorates it the classic way
                                    (using the function call approach)
                                    It works by relying on the cache stored
                                    within the decorator for calls that
                                    have similar signatures.

"""

from ch01_review.find_airport import find_airport
from ch01_review.cache_decorator import cache

# decorate original find_airport function, cache should now work
find_airport = cache(find_airport)


print(find_airport(None, None, 'COS'))              # doesn't use cache
print(find_airport('Albuquerque'))                  # doesn't use cache
print(find_airport(None, None, 'COS'))              # uses cache
print(find_airport('', '', 'COS'))                  # doesn't use cache
print(find_airport('Albuquerque'))                  # uses cache
