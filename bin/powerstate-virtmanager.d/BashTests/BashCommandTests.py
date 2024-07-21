#!/usr/local/bin/python

#
# Filename:       BashCommandTests.py
# Version:        1.0.0
# Description:    BashCommand Unit Tests.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

import sys
import unittest

# TODO: how to call from directory (this is a relative link)
# TODO: create functional unit test.

class BashCommandTests(unittest.TestCase):
  # def __init__(self):
  #   test_GetCommandReturnCode_CommandIsNone_AssertExit(self)
  #   # test_GetCommandReturnCode_CommandIsNotValid_ReturnOutput(self)
  #   # test_GetCommandReturnCode_CommandIsValid_ReturnOutput(self)

  def test_GetCommandReturnCode_CommandIsNone_AssertExit(self):
    exceptionRaised = False

    try:
      result = BashCommand.GetCommandReturnCode(None)
      with self.assertRaises(SystemExit) as systemExit:
        self.assertEqual(systemExit.exception.code, 1)

    except:
      exceptionRaised = True

    self.assertFalse(exceptionRaised)

  # test_GetCommandReturnCode_CommandIsNotValid_ReturnOutput(self)

  # def test_GetCommandReturnCode_CommandIsValid_ReturnOutput(self):
  #   command = "echo \"Hello\""
  #   expected = "Hello"
  #   exceptionRaised = False

  #   try:
  #     result = BashCommand.GetCommandReturnCode(command)

  #   except:
  #     exceptionRaised = True

  #   self.assertFalse(exceptionRaised)
  #   self.assertEqual(result, expected)

if __name__ == '__main__':
  unittest.main()