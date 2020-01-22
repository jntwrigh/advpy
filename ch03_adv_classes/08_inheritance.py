from datetime import date


class Event(object):
    def __init__(self, name='', location='', dt=None):
        self.name = name
        self.location = location
        self.date = dt

    def __str__(self):
        return '{0}'.format(self.name)


class Race(Event):

    def __init__(self, name='', location='', dt=None, distance=0.0, units='km', typ=''):
        Event.__init__(self, name, location, dt)
        self.distance = distance
        self.units = units
        self.type = typ

    def __str__(self):
        return '{0} ({1} {2})'.format(Event.__str__(self), self.distance, self.units)


evt1 = Event('Group Trash Pickup', 'Downtown')
print(evt1)
evt2 = Race('BolderBOULDER', 'Bolder, CO', date(2016, 5, 30), 10, 'km', 'Running')
print(evt2)
