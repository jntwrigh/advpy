"""
        01_fire.py

        Uses the 3rd Party tool: fire.  To use this module:
        1. pip install fire
        2. Run from the command-line (or Run > Edit Configurations... within PyCharm):
               python 01_fire.py display --name "Bolder Boulder" --distance 10 --units km
"""

import fire


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
        return f'{self.name}: {self.distance:.1f} {self.units}'

    def display(self):
        return self.__str__()


if __name__ == '__main__':
    fire.Fire(Race)
