import inspect


class check_args:
    def __init__(self, func):
        self.func = func
        self.annotations = func.__annotations__
        self.argument_names = inspect.getfullargspec(func)[0]       # we are only handling positional args

    def __call__(self, *args):
        checks = []
        retval = '{0} not executed.'.format(self.func.__name__)
        for pos, arg in enumerate(args):                                        # iterate over func arguments
            arg_name = self.argument_names[pos]                                 # get the param name
            annotation = self.annotations.get(arg_name)                         # get the annotation for that name
            if annotation and (type(arg) != self.annotations[arg_name]):        # compare the annotation value to the type check value
                print(f'{arg_name} did not match specified type: {annotation}, got: {type(arg)}')
                checks.append(False)

        if all(checks):                                                         # if checks is empty, all() evaluates to true and the function will be called
            retval = self.func(*args)

        return retval


@check_args
def foo(val):
    return val


@check_args
def bar(val: int, stuff: list=None, more=None):
    return val

print(foo(5))
print(bar('hello'))
print(bar(5, ()))
print(bar(5, []))
