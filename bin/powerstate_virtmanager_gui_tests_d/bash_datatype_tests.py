#!/usr/local/bin/python

#
# Filename:       bash_datatype_tests.py
# Version:        1.0.0
# Description:    BashDatatype Unit Tests.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

# TODO: use https://eli.thegreenplace.net/2011/08/02/python-unit-testing-parametrized-test-cases/

import pytest
import unittest
from unittest.mock  import patch

from bash_command   import BashCommand
from bash_datatype  import BashDatatype

class TestBashDatatype:
  @pytest.mark.parametrize(
    "input",
    [
      None,
      "",
    ],
  )
  def test_GetFormattedArray_InputIsNotValid_DoSystemExit(
    self,
    input
  ):
    with pytest.raises(SystemExit) as contextManager:
      result = BashDatatype.GetFormattedArray(input)

    assert contextManager.value.code == 1

  @pytest.mark.parametrize(
    "input, expected",
    [
      ( "array", "\"${" + "array[*]}\"" ),
    ],
  )
  def test_GetFormattedArray_InputIsValid_ReturnString(
    self,
    input,
    expected
  ):
    result = BashDatatype.GetFormattedArray(input)
    assert result == expected

  @pytest.mark.parametrize(
    "input",
    [
      None,
      "",
    ],
  )
  def test_GetFormattedArrayLength_InputIsNotValid_DoSystemExit(
    self,
    input
  ):
    with pytest.raises(SystemExit) as contextManager:
      result = BashDatatype.GetFormattedArrayLength(input)

    assert contextManager.value.code == 1

  @pytest.mark.parametrize(
    "input, expected",
    [
      ( "array", "\"${" + "#array[*]}\"" ),
    ],
  )
  def test_GetFormattedArrayLength_InputIsValid_ReturnString(
    self,
    input,
    expected
  ):
    result = BashDatatype.GetFormattedArrayLength(input)
    assert result == expected

  @pytest.mark.parametrize(
    "input",
    [
      None,
      "",
    ],
  )
  def test_GetFormattedKeys_InputIsNotValid_DoSystemExit(
    self,
    input
  ):
    with pytest.raises(SystemExit) as contextManager:
      result = BashDatatype.GetFormattedKeys(input)

    assert contextManager.value.code == 1

  @pytest.mark.parametrize(
    "input, expected",
    [
      ( "array", "\"${" + "!array[*]}\"" ),
    ],
  )
  def test_GetFormattedKeys_InputIsValid_ReturnString(
    self,
    input,
    expected
  ):
    result = BashDatatype.GetFormattedKeys(input)
    assert result == expected

  @pytest.mark.parametrize(
    "input",
    [
      None,
      "",
    ],
  )
  def test_GetFormattedVariable_InputIsNotValid_DoSystemExit(
    self,
    input
  ):
    with pytest.raises(SystemExit) as contextManager:
      result = BashDatatype.GetFormattedVariable(input)

    assert contextManager.value.code == 1

  @pytest.mark.parametrize(
    "input, expected",
    [
      ( "variable", "\"${" + "variable}\"" ),
    ],
  )
  def test_GetFormattedVariable_InputIsValid_ReturnString(
    self,
    input,
    expected
  ):
    result = BashDatatype.GetFormattedVariable(input)
    assert result == expected

#   @pytest.mark.parametrize(
#     "input",
#     [
#       None,
#       "",
#     ],
#   )
#   def test_GetFormattedArray_InputIsNotValid_DoSystemExit(
#     self,
#     input
#   ):
#     with self.assertRaises(SystemExit) as contextManager:
#       result = BashDatatype.GetFormattedArray(input)

#     self.assertEqual(contextManager.exception.code, 1)



  # pytest.mark.parametrize(
  #   "input, expected",
  #   [
  #     ( None, "\"\"" ),
  #     ( "", "\"\"" ),
  #     ( "hello", "\"hello\"" ),
  #   ],
  # )
  # def test_GetStringLiteral_ReturnString(
  #   self,
  #   input,
  #   expected
  # ):
  #   result = BashDatatype.GetStringLiteral(input)
  #   self.assertEqual(expected, result)

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