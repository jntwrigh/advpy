class Race(object):

    __slots__ = ('name', 'distance', 'units', 'type', 'location', 'size')

    def __init__(self, name='', distance=0.0, units='km', typ='', location='', size=0):
        self.name = name
        self.distance = distance
        self.units = units
        self.type = typ
        self.location = location
        self.size = size

    def __str__(self):
        return '{0} ({1} {2})'.format(self.name, self.distance, self.units)

    def __repr__(self):
        return '({0}) {1}'.format(self.name, type(self))


race1 = Race('BolderBOULDER', 10, 'km')
# race1.foo = 'hello world'                                  # can't add foo attribute
print(race1.__dict__)                                       # race1 has no __dict__ attribute any longer
