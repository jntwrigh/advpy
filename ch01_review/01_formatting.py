from collections import namedtuple
Winners = namedtuple('Winners', 'first second third')
winners = Winners('Bob', 'Sally', 'John')
print('The winners are: {0}, {1}, {2}'.format(*winners))


from collections import OrderedDict
winners = OrderedDict( third='John' , first='Bob', second='Sally' )
print('The winners are: {first}, {second}, {third}'.format(**winners))


fmt = '{distance:_^+20,.3f}'
distance = 240000
print('Earth to moon distance: {distance:*^+20,.3f} miles'.format(distance=distance))



distance = 240000
width = 20
fmt = '{distance:_^+{width},.3f}'.format(width=width, distance=distance)
print('Earth to moon distance: {fmt} miles'.format(fmt=fmt))


