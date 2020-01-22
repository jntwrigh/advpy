class Race(object):

    def __init__(self, name='', distance=0.0):
        self.name = name
        self._distance = distance

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, distance):
        if distance < 0:
            distance = 0
        self._distance = distance

    def __getattr__(self, attr):
        print('getattr called for: {0}'.format(attr))
        try:
            retval = self.__dict__[attr]
        except KeyError:
            retval = None
        return retval

    def __setattr__(self, attr, value):
        print('setattr called for: {0}'.format(attr))
        if attr in ['_distance', 'distance', 'name']:
            super().__setattr__(attr, value)
        else:
            self.__dict__[attr] = value

    def __str__(self):
        return '{0} ({1})'.format(self.name, self.distance)

race1 = Race('BolderBOULDER', 10)
race1.distance = 6.2
race1.units = 'mi'
print(race1)
print(race1.foo)

