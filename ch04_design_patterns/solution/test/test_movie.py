"""

        test_movie.py       -       Provides tests for testing the resources
                                    in the movie.movie.py module

"""
import unittest

from ch04_design_patterns.solution.movie.movie import Movie


class TestMovie(unittest.TestCase):
    def test_read_only_descriptor(self):
        title = 'Ghostbusters'
        movie = Movie(title)
        movie.title = 'Changed Title'
        self.assertEqual(title, movie.title)