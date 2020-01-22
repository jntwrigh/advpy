"""

    08b_builtin_cache.py       -    This driver imports the find_airport
                                    function, decorates it the classic way
                                    (using the function call approach)
                                    It works by relying on the cache stored
                                    within the decorator for calls that
                                    have similar signatures.

"""

import csv
import functools
from collections import namedtuple


# decorate original find_airport function with std lib cache decorator
@functools.lru_cache(maxsize=None, typed=False)
def find_airport(name='', country='', airport_code='', filename='../resources/airports.dat'):
    results = []
    airport_code = airport_code.upper()

    if not name and not country and not airport_code:
        print('Provide an airport name (name=) or country (country=) or 3-ltr airport code (airport_code)')
        return results

    try:
        with open(filename, encoding='utf8') as f:
            try:
                headings = f.readline().strip()[1:].split(',')                      # [1:] is stripping the \ufeff byte order mark out.
                Airport = namedtuple('Airport', headings)
                for row in csv.reader(f):
                    airport = Airport(*row)
                    if name and country:
                        if (name in airport.name or name in airport.city) and country in airport.country:
                            results.append('{name} ({city}, {country}) Abbr: {IATA_FAA}'.format(**airport._asdict()))
                    elif airport_code and airport_code in airport.IATA_FAA:
                        results.append('{name} ({city}, {country}) Abbr: {IATA_FAA}'.format(**airport._asdict()))
                    else:
                        if name and (name in airport.name or name in airport.city):
                            results.append('{name} ({city}, {country}) Abbr: {IATA_FAA}'.format(**airport._asdict()))
                        elif country and country in airport.country:
                            results.append('{name} ({city}, {country}) Abbr: {IATA_FAA}'.format(**airport._asdict()))

                return results
            except csv.Error as err:
                print(f'Error: {err}')
    except IOError as err:
        print(f'Error with {filename}: {err}')

print(find_airport(None, None, 'COS'))              # doesn't use cache
print(find_airport('Albuquerque'))                  # doesn't use cache
print(find_airport(None, None, 'COS'))              # uses cache
print(find_airport('', '', 'COS'))                  # doesn't use cache
print(find_airport('Albuquerque'))                  # uses cache
print(find_airport.cache_info())
find_airport.clear_cache()
