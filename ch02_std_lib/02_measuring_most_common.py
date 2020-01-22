"""
    02_measuring_most_common.py   -   retrieving the most common item: 3 ways
"""
from collections import Counter, defaultdict
from statistics import mean
import timeit

data = [1, 2, 3, 4, 5, 3, 1, 5, 2, 1, 5, 3, 4, 2, 5]


def most_common_technique1():
    """
        technique 1   -    manually populating a dict
    """
    occurs = {}
    for val in data:
        if val not in occurs.keys():
            occurs[val] = 1
        else:
            occurs[val] += 1

    most_common = sorted(occurs.items(), key=lambda pair: pair[1], reverse=True)
    return most_common[0]


def most_common_technique2():
    """
        technique 2   - using a default dict
    """
    occurs = defaultdict(int)
    for val in data:
        occurs[val] += 1
    most_common = sorted(occurs.items(), key=lambda pair: pair[1], reverse=True)
    return most_common[0]


def most_common_technique3():
    """
        technique 3   -    use of Counter
    """
    return Counter(data).most_common(1)[0]


# repeat() - repeats the 100000 calls 3 times yielding a list of 3 results
iters = 100000
results1 = timeit.repeat('f1()', 'from __main__ import most_common_technique1 as f1', number=iters)
results2 = timeit.repeat('f2()', 'from __main__ import most_common_technique2 as f2', number=iters)
results3 = timeit.repeat('f3()', 'from __main__ import most_common_technique3 as f3', number=iters)


# each results object is a list of 3 values, we can average those:
for idx, results in enumerate([results1, results2, results3], start=1):
    print('Technique {0} avg time to perform {number} iterations: {1:.2f}s'.format(idx, mean(results), number=iters))
