#!/usr/local/bin/python

#
# Filename:       parameterized_test_case.py
# Version:        1.0.0
# Description:    Enables parameters for TestCase classes' unit tests.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

import unittest

class ParameterizedTestCase(unittest.TestCase):
    def __init__(
      self,
      method_name='runTest',
      param=None
    ):
      super(
        ParameterizedTestCase,
        self
      ).__init__(method_name)

      self.param = param

    @staticmethod
    def parameterize(
      test_case_class,
      param=None
    ):
      """ Create a test suite containing all tests taken from the given
          subclass, passing them the parameter 'param'.
      """
      test_loader = unittest.TestLoader()
      test_names = test_loader.getTestCaseNames(test_case_class)
      test_suite = unittest.TestSuite()

      for name in test_names:
          test_suite.addTest(test_case_class(
            name,
            param=param
          ))

      return test_suite