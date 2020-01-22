import collections
import csv


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
                Airport = collections.namedtuple('Airport', headings)
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
