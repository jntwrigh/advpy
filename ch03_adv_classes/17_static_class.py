from contextlib import closing
from urllib.request import urlopen


class Page:
    @staticmethod
    def retrieve(url):
        try:
            with closing(urlopen(url)) as page:
                results = page.read().decode().strip()
        except (ValueError, IOError) as e:
            results = 'Error occurred: {0}'.format(*e.args)
        return results

print(Page.retrieve('http://www.cisco.com'))


class Page2:
    url = 'http://www.google.com'

    @classmethod
    def retrieve(cls):
        try:
            with closing(urlopen(cls.url)) as page:
                results = page.read().decode().strip()
        except (ValueError, IOError) as e:
            results = 'Error occurred: {0}'.format(*e.args)
        return results

print(Page2.retrieve())
