#!/usr/local/bin/python

#
# Filename:       BashDatatypeTests.py
# Version:        1.0.0
# Description:    BashDatatype Unit Tests.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

import unittest
from unittest.mock      import patch
from Bash.BashCommand   import BashCommand
from Bash.BashDatatype  import BashDatatype

class BashCommandTests(unittest.TestCase):
  @pytest.mark.parametrize(
    "input",
    [
      None,
      ""
    ],
  )
  def test_GetFormattedArray_InputIsNotValid_DoSystemExit(
    self,
    input
  ):
    with self.assertRaises(SystemExit) as contextManager:
      result = BashDatatype.GetFormattedArray(input)

    self.assertEqual(contextManager.exception.code, 1)

  @pytest.mark.parametrize(
    "input, expected"
    [
      ( "array", "${\/array[*]}" ),
      ( "variable", "${\/variable[*]}" ),
    ],
  )
  def test_GetFormattedArray_InputIsValid_ReturnString(
    self,
    input,
    expected
  ):
    result = BashDatatype.GetFormattedArray(input)
    self.assertEqual(expected, result)

  pytest.mark.parametrize(
    "input, expected"
    [
      ( None, "\"\"" ),
      ( "", "\"\"" ),
      ( "hello", "\"hello\"" ),
    ],
  )
  def test_GetStringLiteral_ReturnString(
    self,
    input,
    expected
  ):
    result = BashDatatype.GetStringLiteral(input)
    self.assertEqual(expected, result)

  # def test_IsVariable_IsInputNoneOrEmptyString_ThrowSystemExit(self):
  #   with self.assertRaises(SystemExit) as contextManager:
  #     result1 = BashDatatype.IsVariable(None)
  #     result2 = BashDatatype.IsVariable("")

  #   self.assertEqual(contextManager.exception.code, 1)

  # @patch('BashCommand.__init__')
  # def test_IsVariable_IsVariableNameNotValid_ReturnFalse( \
  #   self,
  #   BashCommand_mock
  # ):
  #   BashCommand_mock.code = 1
  #   result = BashDatatype.IsVariable("var")
  #   self.assertFalse(result)
  #   BashCommand_mock.assert_called_once()

  # @patch('BashCommand')
  # def test_IsVariable_IsVariableNameValid_ReturnFalse( \
  #   self,
  #   BashCommand_mock
  # ):
  #   BashCommand_mock.code = 0
  #   result = BashDatatype.IsVariable("var")
  #   self.assertTrue(result)
  #   BashCommand_mock.assert_called_once()

  # @patch('BashCommand')
  # def test_IsVariable_IsVariableNameValid_GetCodeThrowsException_ReturnFalse( \
  #   self,
  #   BashCommand_mock
  # ):
  #   with self.assertRaises(Exception) as contextManager:
  #     result = BashDatatype.IsVariable("var")

  #   self.assertFalse(result)
  #   BashCommand_mock.assert_called_once()

if __name__ == '__main__':
  unittest.main()