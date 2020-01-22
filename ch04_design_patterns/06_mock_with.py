import unittest.mock as mock

import ch04_design_patterns.mock_with_helper as mock_with_helper


def do_something():
    print('__main__.do_something')


with mock.patch('ch04_design_patterns.mock_with_helper.do_something', do_something):
    mock_with_helper.do_something()

mock_with_helper.do_something()
