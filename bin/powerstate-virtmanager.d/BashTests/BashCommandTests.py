#!/usr/local/bin/python

#
# Filename:       BashCommandTests.py
# Version:        1.0.0
# Description:    BashCommand Unit Tests.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

import subprocess
import sys
import unittest
from Bash.BashCommand import BashCommand

# TODO: how to call from directory (this is a relative link)
# TODO: create functional unit test.

class BashCommandTests(unittest.TestCase):
  def test_Example_IfNone_ThrowSysExit(self):
    with self.assertRaises(SystemExit) as contextManager:
      result = BashCommand.Example(None)

    self.assertEqual(contextManager.exception.code, 1)

  def test_Example_IfNotNone_ReturnZero(self):
    result = BashCommand.Example("")
    self.assertEqual(result, 0)

  def test_GetCommandReturnCode_CommandIsNone_ReturnCode(self):
    result = BashCommand.GetCommandReturnCode(None)
    self.assertEqual(result, 127)

  def test_GetCommandReturnCode_CommandDoesNotExist_ReturnCode(self):
    result = BashCommand.GetCommandReturnCode("")
    self.assertEqual(result, 127)

  def test_GetCommandReturnCode_CommandPasses_ReturnZero(self):
    result = BashCommand.GetCommandReturnCode("true")
    self.assertEqual(result, 0)


  def test_GetCommandReturnCode_CommandPasses_ReturnOne(self):
    result = BashCommand.GetCommandReturnCode("false")
    self.assertEqual(result, 1)

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