import os
import urllib.request
import urllib.error


class Operation:
    def __init__(self, value: float):
        self.value = value

    def add(self, second):
        return self.value + second

    def subtract(self, second):
        return self.value - self.value   # purposely incorrect

    def multiply(self, second):
        return self.value * second


def my_function():
    return 'welcome to my_function!'


def get_files(directory):
    return os.listdir(directory)


def only_files(directory):
    if os.path.isdir(directory):
        return [f for f in os.listdir(directory) if os.path.isfile(f)]

    
def get_resource(url):
    try:
        request = urllib.request.Request(url)
        request.add_header('user-agent', 'urllib.py, Python 3.5')
        with urllib.request.urlopen(request) as f:
            results = f.read().decode()
    except (ValueError, urllib.error.URLError) as err:
        results = f'Error: {err}'

    return results
