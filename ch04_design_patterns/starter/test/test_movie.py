"""

        test_movie.py       -       Provides tests for testing the resources
                                    in the movie.movie.py module

"""
import unittest

from ch04_design_patterns.starter.movie.movie import Movie


class TestMovie(unittest.TestCase):
    def test_read_only_descriptor(self):
        # Step 1. Remove the pass statement below.  Then,
        #         create a movie instance, supplying a title
        #         Attempt to change this title after setting it during instantiation
        #         Perform an assertion to see if the original title and movie title are still the same
        pass
