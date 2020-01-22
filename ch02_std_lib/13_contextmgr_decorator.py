from contextlib import ContextDecorator


class ContextMgr(ContextDecorator):
    def __enter__(self):
        print('entering')
        return self

    def __exit__(self, typ, value, traceback):
        print('exiting')
        return False


@ContextMgr()
def f():
    print('the work')


f()
