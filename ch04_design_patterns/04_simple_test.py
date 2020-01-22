import unittest

from ch04_design_patterns.sample import Operation


class TestOperation(unittest.TestCase):

    def setUp(self):
        self.operation = Operation(5)

    def test_add(self):
        second = 5
        actual = self.operation.add(second)
        expected = 10
        self.assertEqual(expected, actual, 'add() not correct')

    def test_subtract(self):
        second = 4
        actual = self.operation.subtract(second)
        expected = 1
        self.assertEqual(expected, actual, 'subtract() not correct')

    def test_multiply(self):
        second = 3
        actual = self.operation.multiply(second)
        expected = 15
        self.assertEqual(expected, actual, 'multiply() not correct')


if __name__ == '__main__':
    unittest.main()
