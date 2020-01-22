def find_it(expr):
    print(f'Searching for: {expr}')
    while True:
        search_str = (yield)
        results = 'Found' if expr.lower() in search_str.lower() else 'Not found'
        print(f'{results} in {search_str}')


g = find_it('happy')
g.__next__()
g.send('Happy birthday to you!')
g.send('Happiness is a state of mind.')
g.send('Stay happy with Python.')
