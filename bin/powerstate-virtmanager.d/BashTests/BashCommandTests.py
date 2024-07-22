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
import Bash.BashCommand # TODO: fix import!

# TODO: how to call from directory (this is a relative link)
# TODO: create functional unit test.

class BashCommandTests(unittest.TestCase):
  def test_GetCommandReturnCode_CommandIsNone_ThrowSystemException(self):
    try:
      result = BashCommand.GetCommandReturnCode(None)
      # with self.assertRaises(SystemExit) as systemExit:
      #   self.assertEqual(systemExit.exception.code, 1)

    except Exception as exception:
      self.assertEqual(exception, SystemExit)
      return

    self.assertFail()

  def test_GetCommandReturnCode_CommandFails_ThrowSubprocessException(self):
    try:
      result = BashCommand.GetCommandReturnCode("false")

    except Exception as exception:
      self.assertEqual(exception, subprocess.CalledProcessError)
      return

    self.assertFail()

  # def test_GetCommandReturnCode_CommandIsValid_ReturnOutput(self):
  #   command = "echo \"Hello\""
  #   expected = "Hello"
  #   isExceptionRaised = False

  #   try:
  #     result = BashCommand.GetCommandReturnCode(command)

  #   except:
  #     isExceptionRaised = True

  #   self.assertFalse(isExceptionRaised)
  #   self.assertEqual(result, expected)

if __name__ == '__main__':
  unittest.main()