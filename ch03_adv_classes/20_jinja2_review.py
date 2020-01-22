from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateError, TemplateNotFound
env = Environment(loader=FileSystemLoader('./tmpl'))


class Race:
    def __init__(self, name='', distance=0.0, units='km'):
        self.name = name
        self.units = units
        self.distance = distance

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

try:
    tmpl = env.get_template('example_tmpl.jinja')
    print(tmpl.render(data=races))
    # can write results to a file as well
except (TemplateNotFound, TemplateError) as e:
    print('Error: {0} {1}'.format(type(e), e))