import urllib.parse
import urllib.request
import urllib.error


def get_resource(url):
    try:
        request = urllib.request.Request(url)
        request.add_header('user-agent', 'urllib.py, Python 3.5')
        with urllib.request.urlopen(request) as f:
            results = f.read().decode()
    except (ValueError, urllib.error.URLError) as err:
        results = f'Error: {err}'

    return results
