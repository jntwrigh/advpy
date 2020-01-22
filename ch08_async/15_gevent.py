import gevent


def func1():
    print('in func1...')
    gevent.sleep(1)
    print('Forcing context switch to func1 again...')


def func2():
    print('in func2...')
    gevent.sleep(1)
    print('Context switch to func2')


gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
])
