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


class Race:
    distance = Convert()                            # comment this line out and run it again

    def __init__(self, name='', distance=0.0, units='mi'):
        self.name = name
        self.units = units                          # caution, distance references units, so it is wise to set units first!
        self.distance = distance

    def __str__(self):
        return '{0}: {1:.1f} {2}'.format(self.name, self.distance, self.units)


race1 = Race('Chicago Marathon', 26.2)
print(race1)

race2 = Race('BolderBOULDER', 10, 'km')
print(race2)

race3 = Race('Hot Chocolate 5k', 16404, 'ft')
print(race3)

race4 = Race('Carlsbad 5000', 5000, 'm')
print(race4)

race5 = Race('Alien Sprint', 100, 'blips')
print(race5)
