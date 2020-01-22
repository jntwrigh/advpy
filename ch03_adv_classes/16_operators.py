from functools import total_ordering
from weakref import WeakKeyDictionary


class Convert:
    conversions = {'mi': 1.0, 'km': 0.621, 'm': 0.000621, 'ft': 0.0001894}

    def __init__(self):
        self.data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self.data.get(instance, 0)

    def __set__(self, instance, value):
        convert_value = self.conversions.get(instance.units.lower(), 0)
        self.data[instance] = value * convert_value
        instance.units = 'mi'


@total_ordering
class Race:
    distance = Convert()        # distance descriptor converts to 'mi'

    def __init__(self, name='', distance=0.0, units='km'):
        self.name = name
        self.units = units
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance

    def __str__(self):
        return '{0} ({1} {2})'.format(self.name, self.distance, self.units)


races = [
    Race('BolderBOULDER', 10000, 'm'),
    Race('Chicago Marathon', 26.2, 'mi'),
    Race('Carlsbad 5000', 5, 'km'),
    Race('Country Music Half Marathon', 13.1, 'mi'),
    Race('Capitol Mile', 5280, 'ft'),
    Race('Peachtree Road Race', 10, 'km'),
]

print(races[5] >= races[0])
races.sort()
for race in races:
    print(race)

