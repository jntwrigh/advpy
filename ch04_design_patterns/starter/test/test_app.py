"""

        test_app.py       -     Provides tests for testing the resources
                                in the app.py module.

"""
import unittest
import unittest.mock as mock
import json

from ch04_design_patterns.starter.app import movie_search, detailed_search, render_movie
from ch04_design_patterns.starter.movie.movie import Movie


class TestApp(unittest.TestCase):

    def setUp(self):
        self.key = '23cf8b21d9a3bfd615076491d6bae442'
        self.search_url = 'http://api.themoviedb.org/3/search/movie?api_key={key}&query={title}'
        self.details_url = 'https://api.themoviedb.org/3/movie/{id}?api_key={key}'

    # Step 2: Add a mock decorator to mock the requests module's get method
    # Note: you must mock the one as used in the app.py directory!
    def test_movie_search(self, request_get):
        with open('fixtures/search_data.dat') as f:
            search_data = f.read()
        # Add one line to set the mock object's (request_get) return value's
        # json() return value to be a dictionary.  Huh? (you might need to read that again)
        # In other words, we are trying to mock:
        #   requests.get(url).json() by returning a dictionary.
        # But not just any dictionary,
        # use the provided fixture data read in from the file at the start of this function.

        # Convert this data to a dictionary and use that dictionary as the return value from the
        # requests.get(url).json() call

        search_dict = movie_search(self.search_url, self.key, 'avengers')
        actual = search_dict.get('results', [])[0]['title']
        expected = 'The Avengers'
        self.assertEqual(expected, actual)

    # Repeat the patch() decorator here in a similar way as the method above
    def test_detailed_search(self, request_get):
        with open('fixtures/details_data.dat') as f:
            details_data = f.read()
        # repeat the mocking of the requests.get().json() return value, this
        # time replacing it with a dict of the details_data above

        actual = detailed_search(self.details_url, self.key, '24480')
        expected = Movie('The Avengers')
        self.assertEqual(expected.title, actual.title)

    def test_render_movie(self, movie):
        movie.title = 'mock title'
        movie.release_date = 'mock release_date'
        movie.runtime = 'mock runtime'
        movie.budget = 0
        movie.revenue = 0
        movie.tagline = 'mock tagline'
        actual = render_movie(movie=movie, tmpl_path='../tmpl')
        with open('fixtures/rendered_movie.dat') as f:
            expected = f.read().strip()
        # perform an assertion to compare results
