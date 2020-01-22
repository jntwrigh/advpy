"""
    05_chained_dicts.py  -   working with multiple dictionaries

    (assumes the student_files directory is on the PYTHONPATH)
"""

from resources.countries import country1, country2, country3
from itertools import chain


for key, val in chain(country1.items(), country2.items(), country3.items()):
    if key == 'name':
        print('{empty:{fill}<{width}}'.format(empty='', fill='-', width=len(val)+4))
        print('{fill} {val} {fill}'.format(val=val, fill='|'))
        print('{empty:{fill}<{width}}'.format(empty='', fill='-', width=len(val)+4))
