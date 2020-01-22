import json
import urllib.request
import urllib.parse

import gevent
from gevent.monkey import patch_socket
patch_socket()


class MovieGreenlet(gevent.Greenlet):
    key = '23cf8b21d9a3bfd615076491d6bae442'
    search_url = 'http://api.themoviedb.org/3/search/movie?api_key={key}&query={title}'

    def __init__(self, search_val=None):
        gevent.Greenlet.__init__(self)
        self.search_val = urllib.parse.quote_plus(search_val)

    def _run(self):
        if self.search_val is not None:
            print('Searching...')
            print(self.search())

    def search(self):
        response = urllib.request.urlopen(MovieGreenlet.search_url.format(key=MovieGreenlet.key, title=self.search_val))
        result = response.read().decode()
        json_result = json.loads(result)
        return 'Found: ' + json_result['results'][0]['title']


search_terms = ['amazing spiderman', 'iron man', 'thor', 'hulk']
movie_greenlets = [MovieGreenlet(search) for search in search_terms]

for m in movie_greenlets:
    m.start()

gevent.joinall(movie_greenlets)
