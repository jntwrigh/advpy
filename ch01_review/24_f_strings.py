from collections import namedtuple
Winners = namedtuple('Winners', 'first second third')

first = 'bob'
last = 'Smith'
age = 37


def combine():
    return first + ' ' + last


print(f'{first.capitalize()} {last} {age} {combine()}')


winners = Winners('Bob', 'Sally', 'John')
# f-strings do not support the expansion (unpack) operator very well
print(f'The winners are: {" ".join(str(x) for x in winners)}')           # this works but isn't ideal


winners = {'first': 'Bob', 'second': 'Sally', 'third': 'John'}
print(f'The winners are: {winners.get("first")} {winners["second"]} {list(winners.values())[2]}')


distance = 240000
width = 25

fmt = f'{distance:_^+20,.3f}'
print(f'Earth to moon distance: {fmt} miles')

fmt = f'{distance:_^+{width},.3f}'
print(f'Earth to moon distance: {fmt} miles')