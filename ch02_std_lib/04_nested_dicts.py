"""
    04_nested_dicts.py  -   how to safely access nested dictionaries

    (assumes the student_files directory is on the PYTHONPATH)
"""

from resources.countries import countries

# this one is okay
print(countries['usa']['regions']['california']['name'])


# but what if it is not?-->this yields a KeyError
# print(countries['usa']['region']['california']['name'])



result = countries.get('usa', {}).get('regions', {}).get('california', {}).get('name')
print(result)


d = countries
try:
    for key in ['usa', 'regions', 'california', 'name']:
        d = d[key]
except KeyError:
    result = None
print(result)


result = None
try:
    result = countries.get('usa').get('regions').get('california').get('name')
except AttributeError:
    pass
print(result)
