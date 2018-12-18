# Code from:
# https://www.internalpointers.com/post/run-painless-test-suites-python-unittest

import unittest

import test_ioc
import test_iocfile
import test_iocargs

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_ioc))
suite.addTests(loader.loadTestsFromModule(test_iocfile))
suite.addTests(loader.loadTestsFromModule(test_iocargs))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
