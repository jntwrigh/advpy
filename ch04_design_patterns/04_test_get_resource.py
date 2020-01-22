import unittest
from ch04_design_patterns.sample import get_resource


class TestGetResource(unittest.TestCase):
    def setUp(self):
        self.url = 'https://www.cisco.com/c/en/us/solutions/enterprise/design-zone-ipv6/index.html'

    def test_get_resource(self):
        expected_len = 55873
        actual_len = len(get_resource(self.url))
        self.assertEqual(expected_len, actual_len)


if __name__ == '__main__':
    unittest.main()
