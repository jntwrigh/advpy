import unittest
import unittest.mock as mock
from ch04_design_patterns.sample import only_files


def os_path_isfile_mock(f):
    return True if not f == 'not_file' else False


class TestOnlyFiles(unittest.TestCase):
    @mock.patch('os.path.isfile', return_value=True)
    @mock.patch('os.path.isdir', return_value=True)
    @mock.patch('os.listdir', return_value=['a', 'b', 'c'])
    def test_only_files_normal(self, os_listdir, os_path_isdir, os_path_isfile):
        actual = only_files('foo')
        expected = ['a', 'b', 'c']
        self.assertSequenceEqual(expected, actual)

    @mock.patch('os.path.isdir', return_value=False)
    def test_only_files_not_directory(self, os_listdir):
        actual = only_files('foo')
        self.assertIsNone(actual)

    @mock.patch('os.path.isfile', side_effect=os_path_isfile_mock)
    @mock.patch('os.path.isdir', return_value=True)
    @mock.patch('os.listdir', return_value=['a', 'b', 'c'])
    def test_only_files_non_file(self, os_listdir, os_path_isdir, os_path_isfile):
        actual = only_files('foo')
        expected = ['a', 'b', 'c']
        self.assertSequenceEqual(expected, actual)

        os_listdir.return_value = ['a', 'not_file', 'c']
        actual = only_files('foo')
        expected = ['a', 'c']
        self.assertSequenceEqual(expected, actual)