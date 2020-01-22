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


class Race(object):
    distance = Convert()

    def __init__(self, name, distance=0.0, units='km'):
        self.name = name
        self.units = units
        self.distance = distance

    @classmethod
    def race10k(cls, name):
        return cls(name, 10, 'km')

    @classmethod
    def race_marathon(cls, name):
        return cls(name, 26.2, 'mi')

    def __str__(self):
        return f'{self.name} ({self.distance} {self.units})'

    __repr__ = __str__


race1 = Race('Carlsbad 5000', 5, 'km')
race2 = Race.race10k('BolderBOULDER')
race3 = Race.race_marathon('Chicago Marathon')

print(race1, race2, race3)
