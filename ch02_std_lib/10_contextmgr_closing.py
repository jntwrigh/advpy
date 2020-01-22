from contextlib import closing
from urllib.request import urlopen
from urllib.error import URLError

url = 'http://www.cisco.com'
try:
    with closing(urlopen(url)) as page:
        results = page.read()
except URLError:
    results = b'Error retrieving page'

print(results.decode().strip())


class Work:
    def __init__(self):
        pass

    def do_work(self):
        print('doing work...')

    def close(self):
        print('Closed!')

with closing(Work()) as work:
    work.do_work()

