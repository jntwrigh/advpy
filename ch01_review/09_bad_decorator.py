"""
    09_bad_decorator.py     -   This example shows what NOT to do with a
                                decorator.  It attempts to make a function
                                automatically close a file.

                                It changes the arguments of
                                the original function from a file object
                                and data to a filename (str), data, and
                                perhaps other stuff.  Don't create decorators
                                that force the changing of arguments
                                (as this example does).
"""
def manage_file(func):
    def wrapper(filename, data='', mode='wt', encoding='utf-8', *args, **kwargs):
        with open(filename, mode=mode, encoding=encoding) as f:
            return func(f, data, *args, **kwargs)
    return wrapper


@manage_file
def write_data(f, data):
    for line in data:
        f.write(f'{line}\n')


data = [
    'This is data that will be',
    'written out to the specified',
    'file and close automatically.'
]
write_data('somefile.txt', data)
