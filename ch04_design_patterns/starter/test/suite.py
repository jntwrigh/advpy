"""

        suite.py            -       Provides a single file to locate all
                                    test modules in the specified test_dir
                                    test directory and load them into a
                                    test suite.  Simply by running this file
                                    as a test file, all tests will be run.

"""
import glob
import unittest

test_package = 'ch04_design_patterns.solution.test'
test_dir = '.'
test_modules = [test_mod[:-3] for test_mod in glob.glob('test*.py')]

suite = unittest.TestLoader()
fullnames = ['{0}.{1}'.format(test_package, mod) for mod in test_modules]
print('Testing the following modules: {0}'.format(fullnames))
suite = suite.loadTestsFromNames(fullnames)

unittest.TextTestRunner().run(suite)
