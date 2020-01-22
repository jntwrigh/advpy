import unittest
import unittest.mock as mock
import contextlib
from ch04_design_patterns.book_request import get_resource


class MockResponse:
    def __init__(self, resp_data=b''):
        self.resp_data = resp_data

    def read(self):
        return self.resp_data


@contextlib.contextmanager
def urlopen_mock(url):
    yield MockResponse(b'return from urlopen_mock')


class TestGetResource(unittest.TestCase):
    @mock.patch('ch04_design_patterns.book_request.urllib.request.urlopen', side_effect=urlopen_mock)
    def test_get_resource(self, urlopen):
        actual = get_resource('http://some_url')
        expected = 'return from urlopen_mock'
        self.assertEqual(expected, actual)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
