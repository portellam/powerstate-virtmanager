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
  def test_GetCommandReturnCode_command_is_none_do_exit(self):
    exceptionRaised = false

    try:
      result = BashCommand.GetCommandReturnCode(None)
      with self.assertRaises(SystemExit) as systemExit:
        self.assertEqual(systemExit.exception.code, 1)

    except:
      exceptionRaised = true

    self.assertFalse(exceptionRaised)

  # test_GetCommandReturnCode_command_is_not_valid_return_output(self)

  # def test_GetCommandReturnCode_command_is_valid_return_output(self):
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