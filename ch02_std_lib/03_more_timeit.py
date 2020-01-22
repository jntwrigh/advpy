"""
    03_more_timeit.py   -   shows the use of the module's class
                            implementation.
"""
import timeit
t = timeit.Timer(stmt="print('hello world')", setup="print('setup')")
print(t.timeit(2))
print(t.repeat(repeat=3, number=2))
