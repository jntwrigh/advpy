class Race(object):

    def __init__(self, name='', distance=0.0, units='km', typ='', location='', size=0):
        self.name = name
        self.distance = distance
        self.units = units
        self.type = typ
        self.location = location
        self.size = size

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, distance):
        if distance < 0:
            distance = 0
        self._distance = distance

    def __str__(self):
        return '{0} ({1} {2})'.format(self.name, self.distance, self.units)

    def __repr__(self):
        return '({0}) {1}'.format(self.name, type(self))


race1 = Race('BolderBOULDER', -10, 'km')
print(race1)
