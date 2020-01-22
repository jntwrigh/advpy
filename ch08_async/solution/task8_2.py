"""

    solution/task 8_2.py    -           This file makes a single request to the
                                        first host listed in this file.  And displays
                                        their HTTP header information.

                                        Your task is to rework this using gevent and
                                        to make a request to ALL of the hosts retrieving
                                        their headers.

"""
from urllib.request import urlopen
from contextlib import closing

import gevent
from gevent.monkey import patch_socket

patch_socket()

hosts = [
        'www.google.com', 'www.yahoo.com', 'www.cisco.com',
        'www.yelp.com', 'www.im_not_real.com', 'www.espn.com',
        'www.walmart.com', 'www.twitter.com', 'www.facebook.com',
        'www.youtube.com', 'www.wikipedia.org', 'www.go.com',
        'www.ebay.com', 'www.weather.com', 'www.bing.com',
        'www.craigslist.org', 'www.reddit.com', 'www.pinterest.com',
        'www.linkedin.com', 'www.huffingtonpost.com', 'www.apple.com',
        'www.cnn.com', 'www.nytimes.com', 'www.blogspot.com',
        'www.microsoft.com'
    ]


def get_headers(url):
    print('Reading {0}'.format(url))
    try:
        with closing(urlopen('http://{url}'.format(url=url))) as page:
            headers = page.getheaders()
            print('Server Response Headers: {0}'.format(' '.join(['{0}: {1},'.format(*header) for header in headers])))
    except (ValueError, IOError):
        pass

jobs = []
for host in hosts:
    jobs.append(gevent.spawn(get_headers, host))

gevent.joinall(jobs)
