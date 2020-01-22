class Foo(object):
    def __init__(self):
        self.bar = 10
        self.baz = 20

    def __getattribute__(self, attr):
        if attr == 'bar':
            return 'hello'

        return object.__getattribute__(self, attr)


f = Foo()
f.something_else = 30
print(f.bar, f.baz, f.something_else)
