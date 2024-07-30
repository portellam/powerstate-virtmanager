#!/usr/local/bin/python

#
# Filename:       bash_command_tests.py
# Version:        1.0.0
# Description:    BashCommand Unit Tests.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

import subprocess
import sys

import pytest
import unittest
from unittest.mock  import Mock, patch

from bash_command   import BashCommand

# TODO: how to call from directory (this is a relative link)
# TODO: create functional unit test.

class BashCommandTests(unittest.TestCase):
  @patch('sys.stdin.readline')
  def test_GetInput_ReadlineReturnsNonEmptyString_ReturnString(
    self,
    mock_readline
  ):
    mock_readline.return_value = "Hello World"
    bashCommand = BashCommand("echo \"Hello World\"")
    result = bashCommand.GetInput()
    assert result == "Hello World"
    mock_readline.assert_called_once()

  @patch('sys.stdin.readline')
  def test_GetInput_ReadlineReturnsEmptyString_ReturnEmptyString(
    self,
    mock_readline
  ):
    mock_readline.return_value = ""
    bashCommand = BashCommand("")
    result = bashCommand.GetInput()
    assert result == ""
    mock_readline.assert_called_once()

  @patch('sys.stdin.readline')
  def test_GetInput_ReadlineReturnsNone_ThrowSystemExit(
    self,
    mock_readline
  ):
    mock_readline.return_value = None
    bashCommand = BashCommand("")

    with pytest.raises(SystemExit) as contextManager:
      result = bashCommand.GetInput()

    assert contextManager.value.code == 1
    mock_readline.assert_called_once()

  # @patch('sys.stdin')
  # def test_GetInput_ReadlineThrowsException_ReturnNone(
  #   self,
  #   mock_stdin
  # ):
  #   mock_stdin.readline.raiseError.side_effect = Mock(
  #     side_effect=Exception()
  #   )

  #   bashCommand = BashCommand(None)

    # with pytest.raises(SystemExit) as contextManager:
    #   result = bashCommand.GetInput()

    # mock_stdin.assert_called_once()
    # assert contextManager.value.code == 1

    # result = bashCommand.GetInput().return_value
    # assert result == None

  # @mock.patch('BashCommand.GetInput')
  # def test_SetInput_CommandIsNone_SetProperties(self, GetInputMock):
  #   GetInputMock.return_value = ""
  #   result = BashCommand()

  #   BashCommand().SetInput()

  #   assertEqual(result.command, "")

  # @patch('sys.stdin.readline')
  # def test_GetInput_InputIsNone_ReturnNone( \
  #   self,
  #   mock_readline
  # ):
  #   mock_readline.return_value = None
  #   bashCommand = BashCommand(None)
  #   result = bashCommand.GetInput()

  #   self.assertEqual(
  #     result,
  #     None
  #   )

  #   mock_readline.assert_called_once()

  # @patch('sys.stdin.readline')
  # def test_GetInput_InputIsString_ReturnExactString( \
  #   self,
  #   mock_readline
  # ):
  #   mock_readline.return_value = "echo \"Hello World\""
  #   bashCommand = BashCommand(None)
  #   result = bashCommand.GetInput()

  #   self.assertEqual(
  #     result,
  #     "echo \"Hello World\""
  #   )

  #   mock_readline.assert_called_once()

 # def test_GetCode_CommandDoesNotExist_ReturnExpectedCode(self):
  #   result = BashCommand.GetCode("")
  #   self.assertEqual(result, 127)

  # def test_GetCode_CommandIsNone_ReturnExpectedCode(self):
  #   result = BashCommand.GetCode(None)
  #   self.assertEqual(result, 127)

  # def test_GetCode_CommandPasses_ReturnOne(self):
  #   result = BashCommand.GetCode("false")
  #   self.assertEqual(result, 1)

  # def test_GetCode_CommandPasses_ReturnZero(self):
  #   result = BashCommand.GetCode("true")
  #   self.assertEqual(result, 0)

  # def test_GetOutput_CommandDoesNotExist_ReturnEmptyString(self):
  #   result = BashCommand.GetOutput("")
  #   self.assertEqual(result, "")

  # def test_GetOutput_CommandIsNone_ReturnNone(self):
  #   result = BashCommand.GetOutput(None)
  #   self.assertEqual(result, None)

  # def test_GetOutput_CommandIsString_ReturnOutput(self):
  #   expected = "Hello World"

  #   command = "echo \"{}\"" \
  #             .format("Hello World")

  #   result = BashCommand.GetOutput(command)

  #   print(command)

if __name__ == '__main__':
  unittest.main()