"""
    19_getsizeof.py     -    Run this in different interpreters 2.7 - 3.6 to see
                             the sizes of various Python data structures
"""
import sys


class ClassicClasses:
    pass


class NewStyleClasses(object):
    pass


class SlotsBasedClasses(object):
    __slots__ = ()


for item in [], (), {}, 'a', 'some_string', 1, 2.3, ClassicClasses, ClassicClasses(), \
            NewStyleClasses, NewStyleClasses(), SlotsBasedClasses, SlotsBasedClasses():
    typ = type(item).__name__
    size = sys.getsizeof(item)
    print('{0:<20} : {1}'.format(typ, size))
