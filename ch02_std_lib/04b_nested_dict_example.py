"""
    04b nested dict example - the following example uses the request module to
    retrieve LIVE data containing nested dictionaries (and lists).

    Direct access can sometimes be problematic if you wish to ensure code
    "survives" conditions where expected data is not present.

    To help, the use of default dictionary values and error handling can help
    achieve safer results.
"""
import requests


def get_incidents(url):
    results = requests.get(url).json()

    # live data that accesses a list of dictionaries within a dictionary
    name = results['markers'][0]['name']
    print(name)

    try:
        name = results.get('markers', [])[0].get('name', {})
    except IndexError:
        name = None

    print(name)

url = 'https://inciweb.nwcg.gov/feeds/json/markers/'
get_incidents(url)
