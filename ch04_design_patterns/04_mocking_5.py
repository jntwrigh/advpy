import unittest
import unittest.mock as mock
import urllib.error
from ch04_design_patterns.sample import get_resource


class TestGetResource(unittest.TestCase):
    @mock.patch('ch04_design_patterns.sample.urllib.request.urlopen')
    def test_get_resource(self, urlopen):
        urlopen.return_value.read.return_value = b'returned urlopen test value'
        actual = get_resource('http:/some_url')
        expected = 'returned urlopen test value'
        self.assertEqual(expected, actual)

    @mock.patch('ch04_design_patterns.sample.urllib.request.urlopen')
    def test_get_resource_for_errors(self, urlopen):
        urlopen.side_effect = Exception('should be raised')
        self.assertRaises(Exception, get_resource, 'http://some_url')

        urlopen.side_effect = ValueError('testing ValueError')
        self.assertEqual('Error: testing ValueError', get_resource('http://some_url'))

        urlopen.side_effect = urllib.error.URLError('testing URLError')
        self.assertEqual('Error: <urlopen error testing URLError>', get_resource('http://some_url'))
