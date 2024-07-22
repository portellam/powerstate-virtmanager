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
  def test_GetCode_CommandDoesNotExist_ReturnExpectedCode(self):
    result = BashCommand.GetCode("")
    self.assertEqual(result, 127)

  def test_GetCode_CommandIsNone_ReturnExpectedCode(self):
    result = BashCommand.GetCode(None)
    self.assertEqual(result, 127)

  def test_GetCode_CommandPasses_ReturnOne(self):
    result = BashCommand.GetCode("false")
    self.assertEqual(result, 1)

  def test_GetCode_CommandPasses_ReturnZero(self):
    result = BashCommand.GetCode("true")
    self.assertEqual(result, 0)

  def test_GetOutput_CommandDoesNotExist_ReturnEmptyString(self):
    result = BashCommand.GetOutput("")
    self.assertEqual(result, "")

  def test_GetOutput_CommandIsNone_ReturnNone(self):
    result = BashCommand.GetOutput(None)
    self.assertEqual(result, None)

  def test_GetOutput_CommandIsString_ReturnOutput(self):
    expected = "Hello World"

    command = "echo \"{}\"" \
              .format("Hello World")

    result = BashCommand.GetOutput(command)

    print(command)
    # self.assertEqual(result, expected)

  # def test_GetCode_CommandIsValid_ReturnOutput(self):
  #   command = "echo \"Hello\""
  #   expected = "Hello"
  #   isExceptionRaised = False

  #   try:
  #     result = BashCommand.GetCode(command)

  #   except:
  #     isExceptionRaised = True

  #   self.assertFalse(isExceptionRaised)
  #   self.assertEqual(result, expected)

if __name__ == '__main__':
  unittest.main()