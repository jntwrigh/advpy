import unittest
import unittest.mock as mock
from ch04_design_patterns.sample import get_files


class TestGetFiles(unittest.TestCase):
    @mock.patch('os.listdir', return_value=['a', 'b', 'c'])
    def test_get_files(self, os_listdir):
        actual = get_files('foo')
        expected = ['a', 'b', 'c']
        self.assertSequenceEqual(expected, actual, 'different return from os.listdir')
        self.assertTrue(os_listdir.call_count == 1)
        self.assertTrue(os_listdir.called)
