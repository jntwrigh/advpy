def decorator(a_func):
    def modified(name):
        print('I have been enhanced.')
        return a_func(name)
    return modified


def my_func(name):
    print(f'Hello {name}')


@decorator
def my_func2(name):
    print(f'Welcome {name}')


my_func = decorator(my_func)

my_func('Bob')
my_func2('Sally')
