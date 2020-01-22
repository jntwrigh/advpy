class Race(object):

    def __init__(self, name='', distance=0.0, units='km', typ='', location='', size=0):
        """
            You can use the constructor in many ways:
            Race() - void arguments
            Race('NYC Marathon', 26.2, 'mi') - passing two arguments
            Race('NYC Marathon', units='mi', distance=26.2) - passing keywords arguments
            Race(**{'name': 'NYC Marathon','distance': 10, 'units': 'km'}) - unpacking a dictionary
            Race(*['NYC Marathon', 26.2, 'km']) - unpacking a list or a tuple (or a generic iterable)
            Race(*Race('NYC Marathon', 26.2, 'km')) - copy constructor (unpack the Race itself)
        """
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
race2 = Race('Chicago Marathon', 26.2, 'mi', location='Chicago, IL', typ='running')
print(race1)
print([race1, race2])
