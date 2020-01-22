"""
    20_simple_pstats.py     -   Run this as is in PyCharm or uncomment the code at
                                the bottom to run using the cProfile module.
                                Call f2() or f3() a second time to better understand
                                the cumtime vs percall.
"""
import time


def f1():
    print('in f1')
    time.sleep(1)
    f2()


def f2():
    print('in f2')
    time.sleep(1)
    f3()


def f3():
    print('in f3')
    time.sleep(1)

f1()


"""
# uncomment the multi-line string here to run cProfile outside of Pycharm
if __name__ == '__main__':
    import cProfile, pstats
    cProfile.run('f1();f2()', 'stats_results')

    p = pstats.Stats('stats_results')
    p.print_stats()
    p.strip_dirs().print_stats()
    p.strip_dirs().sort_stats('ncalls', 'time')
"""
