import unittest
import unittest.mock as mock
from ch04_design_patterns.sample import get_files


def os_listdir_mock(dir):
    return ['a', 'b', 'c', dir]


class TestGetFiles(unittest.TestCase):
    @mock.patch('os.listdir', side_effect=os_listdir_mock)
    def test_get_files(self, os_listdir):
        print(type(os_listdir.side_effect))
        actual = get_files('foo')
        expected = ['a', 'b', 'c', 'foo']
        self.assertEqual(expected, actual)
