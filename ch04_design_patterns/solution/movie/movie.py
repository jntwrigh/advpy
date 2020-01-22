"""

    movie.py    -   Contains classes related to encapsulating a movie.

    The constructors use capital letters to match the incoming JSON-data
    and therefore allow for easier unpacking.

"""
import abc
import weakref


class ReadOnly(object):
    def __init__(self):
        self.data = weakref.WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self.data.get(instance, '')

    def __set__(self, instance, value):
        if not self.data.get(instance):
            self.data[instance] = value


class Media(abc.ABC):
    title = ReadOnly()

    @abc.abstractmethod
    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def __str__(self):
        return f'{self.title} ({self.release_date})'


class Movie(Media):
    def __init__(self, title='', release_date=None, runtime=0,
                 budget=0, revenue=0, tagline='', **kwargs):
        super().__init__(title, release_date)
        self.runtime = runtime
        self.budget = budget
        self.revenue = revenue
        self.tagline = tagline
        self.extras = kwargs

    def __str__(self):
        return f'{super().__str__()} [${self.revenue:,}]'
