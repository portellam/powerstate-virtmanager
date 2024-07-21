#!/usr/local/bin/python

#
# Filename:       BashCommandTests.py
# Version:        1.0.0
# Description:    BashCommand Unit Tests.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

import unittest
import ..Bash.BashCommand

# TODO: how to call from directory (this is a relative link)
# TODO: create functional unit test.

class BashCommandTests(unittest.TestCase):
  def Test_GetCommandReturnCode_CommandIsNone_AssertExit(self):
    exceptionRaised = false

    try:
      result = BashCommand.GetCommandReturnCode(None)
      with self.assertRaises(SystemExit) as systemExit:
        self.assertEqual(systemExit.exception.code, 1)

    except:
      exceptionRaised = true

    self.assertFalse(exceptionRaised)

  # Test_GetCommandReturnCode_CommandIsNotValid_ReturnOutput(self)

  # def Test_GetCommandReturnCode_CommandIsValid_ReturnOutput(self):
  #   command = "echo \"Hello\""
  #   expected = "Hello"
  #   exceptionRaised = false

  #   try:
  #     result = BashCommand.GetCommandReturnCode(command)

  #   except:
  #     exceptionRaised = true

  #   self.assertFalse(exceptionRaised)
  #   self.assertEqual(result, expected)

if __name__ == '__main__':
  unittest.main()