import json
import urllib.request

import gevent
import gevent.monkey
gevent.monkey.patch_all()

key = '23cf8b21d9a3bfd615076491d6bae442'
search_url = 'http://api.themoviedb.org/3/search/movie?api_key={key}&query={title}'


def task(id, search_val):
    print('Task {0}'.format(id))
    gevent.sleep(0)
    response = urllib.request.urlopen(search_url.format(key=key, title=search_val))
    result = response.read().decode()
    json_result = json.loads(result)
    print(json_result['results'][0]['title'])


def five_tasks(search_val):
    print('Without gevent: ')
    for i in range(5):
        task(i, search_val)


def five_tasks_async(search_val):
    print('Now using gevent: ')
    jobs = [gevent.spawn(task, i, search_val) for i in range(5)]
    gevent.joinall(jobs)


search_val = input('Movie search term --> ')
five_tasks(search_val)
five_tasks_async(search_val)
