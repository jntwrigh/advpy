class CtxMgr(object):
    def __enter__(self):
        print('enter')
        return 'foo'

    def __exit__(self, typ, value, traceback):
        print('exiting')
        return True


with CtxMgr() as obj:
    int(obj)    # raises ValueError
    print(obj)  # never seen
