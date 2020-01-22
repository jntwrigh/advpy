"""

        test_app.py       -     Provides tests for testing the resources
                                in the app.py module.

"""
import unittest
import unittest.mock as mock
import json

from ch04_design_patterns.solution.app import movie_search, detailed_search, render_movie
from ch04_design_patterns.solution.movie.movie import Movie


class TestApp(unittest.TestCase):

    def setUp(self):
        self.key = '23cf8b21d9a3bfd615076491d6bae442'
        self.search_url = 'http://api.themoviedb.org/3/search/movie?api_key={key}&query={title}'
        self.details_url = 'https://api.themoviedb.org/3/movie/{id}?api_key={key}'

    @mock.patch('ch04_design_patterns.solution.app.requests.get')
    def test_movie_search(self, request_get):
        with open('fixtures/search_data.dat') as f:
            search_data = f.read()

        request_get.return_value.json.return_value = json.loads(search_data)

        search_dict = movie_search(self.search_url, self.key, 'avengers')
        actual = search_dict.get('results', [])[0]['title']
        expected = 'The Avengers'
        self.assertEqual(expected, actual)

    @mock.patch('ch04_design_patterns.solution.app.requests.get')
    def test_detailed_search(self, request_get):
        with open('fixtures/details_data.dat') as f:
            details_data = f.read()
        request_get.return_value.json.return_value = json.loads(details_data)
        actual = detailed_search(self.details_url, self.key, '24480')
        expected = Movie('The Avengers')
        self.assertEqual(expected.title, actual.title)

    @mock.patch('ch04_design_patterns.solution.movie.movie.Movie')
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
        self.assertEqual(expected, actual)
