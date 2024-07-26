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
      "my_variable",
      "ENVIRONMENT_VARIABLE",
      "Abc123_",
    ],
  )
  def test_IsReferenceLegal_InputIsLegal_ReturnTrue(
    self,
    input,
  ):
    result = BashDatatype.IsReferenceLegal(input)
    assert result == True

  @pytest.mark.parametrize(
    "input",
    [
      None,
      "",
      "+",
      "Abc123+",
      "-",
      "Abc123-"
    ],
  )
  def test_IsReferenceLegal_InputIsNotLegal_ReturnFalse(
    self,
    input,
  ):
    result = BashDatatype.IsReferenceLegal(input)
    assert result == False

  # @pytest.mark.parametrize(
  #   "input",
  #   [
  #     None,
  #     "",
  #   ],
  # )
  # def test_GetFormattedArray_InputIsNotValid_DoSystemExit(
  #   self,
  #   input,
  # ):
  #   with pytest.raises(SystemExit) as contextManager:
  #     result = BashDatatype.GetFormattedArray(input)

  #   assert contextManager.value.code == 1

  # @pytest.mark.parametrize(
  #   "input, expected",
  #   [
  #     ( "array", "\"${" + "array[*]}\"" ),
  #   ],
  # )
  # def test_GetFormattedArray_InputIsValid_ReturnString(
  #   self,
  #   input,
  #   expected,
  # ):
  #   result = BashDatatype.GetFormattedArray(input)
  #   assert result == expected

  # @pytest.mark.parametrize(
  #   "input",
  #   [
  #     None,
  #     "",
  #   ],
  # )
  # def test_GetFormattedArrayLength_InputIsNotValid_DoSystemExit(
  #   self,
  #   input,
  # ):
  #   with pytest.raises(SystemExit) as contextManager:
  #     result = BashDatatype.GetFormattedArrayLength(input)

  #   assert contextManager.value.code == 1

  # @pytest.mark.parametrize(
  #   "input, expected",
  #   [
  #     ( "array", "\"${" + "#array[*]}\"" ),
  #   ],
  # )
  # def test_GetFormattedArrayLength_InputIsValid_ReturnString(
  #   self,
  #   input,
  #   expected,
  # ):
  #   result = BashDatatype.GetFormattedArrayLength(input)
  #   assert result == expected

  # @pytest.mark.parametrize(
  #   "input",
  #   [
  #     None,
  #     "",
  #   ],
  # )
  # def test_GetFormattedKeys_InputIsNotValid_DoSystemExit(
  #   self,
  #   input,
  # ):
  #   with pytest.raises(SystemExit) as contextManager:
  #     result = BashDatatype.GetFormattedKeys(input)

  #   assert contextManager.value.code == 1

  # @pytest.mark.parametrize(
  #   "input, expected",
  #   [
  #     ( "array", "\"${" + "!array[*]}\"" ),
  #   ],
  # )
  # def test_GetFormattedKeys_InputIsValid_ReturnString(
  #   self,
  #   input,
  #   expected,
  # ):
  #   result = BashDatatype.GetFormattedKeys(input)
  #   assert result == expected

  # @pytest.mark.parametrize(
  #   "input",
  #   [
  #     None,
  #     "",
  #   ],
  # )
  # def test_GetFormattedVariable_InputIsNotValid_DoSystemExit(
  #   self,
  #   input,
  # ):
  #   with pytest.raises(SystemExit) as contextManager:
  #     result = BashDatatype.GetFormattedVariable(input)

  #   assert contextManager.value.code == 1

  # @pytest.mark.parametrize(
  #   "input, expected",
  #   [
  #     ( "variable", "\"${" + "variable}\"" ),
  #   ],
  # )
  # def test_GetFormattedVariable_InputIsValid_ReturnString(
  #   self,
  #   input,
  #   expected,
  # ):
  #   result = BashDatatype.GetFormattedVariable(input)
  #   assert result == expected

  # @pytest.mark.parametrize(
  #   "input",
  #   [
  #     None,
  #     "",
  #   ],
  # )
  # def test_GetKeysOutput_InputIsNotValid_ThrowSystemExit(
  #   self,
  #   input,
  # ):
  #   with pytest.raises(SystemExit) as contextManager:
  #     result = BashDatatype.GetKeysOutput(input)

  #   assert contextManager.value.code == 1

  # # test_GetKeysOutput_InputIsValid_ReturnOutput

  # @pytest.mark.parametrize(
  #   "input",
  #   [
  #     None,
  #     "",
  #   ],
  # )
  # def test_GetVariableOutput_InputIsNotValid_ThrowSystemExit(
  #   self,
  #   input,
  # ):
  #   with pytest.raises(SystemExit) as contextManager:
  #     result = BashDatatype.GetVariableOutput(input)

  #   assert contextManager.value.code == 1

  # # test_GetVariableOutput_InputIsValid_ReturnOutput

  # @pytest.mark.parametrize(
  #   "input",
  #   [
  #     None,
  #     "",
  #   ],
  # )
  # def test_GetStringLiteral_InputIsNullOrEmptyString_ReturnEmptyString(
  #   self,
  #   input,
  # ):
  #   expected = "\"\""
  #   result = BashDatatype.GetStringLiteral(input)
  #   assert result == expected

  # @pytest.mark.parametrize(
  #   "input, expected",
  #   [
  #     ( "hello", "\"hello\"" ),
  #     ( "world", "\"world\"" ),
  #   ],
  # )
  # def test_GetStringLiteral_InputIsNonEmptyString_ReturnString(
  #   self,
  #   input,
  #   expected,
  # ):
  #   result = BashDatatype.GetStringLiteral(input)
  #   assert result == expected

  # @pytest.mark.parametrize(
  #   "input",
  #   [
  #     None,
  #     "",
  #   ],
  # )
  # def test_IsArray_InputIsNotValid_ThrowSystemExit(
  #   self,
  #   input,
  # ):
  #   with pytest.raises(SystemExit) as contextManager:
  #     result = BashDatatype.IsArray(input)

  #   assert contextManager.value.code == 1

  # # test_IsArray_InputIsValid_ReturnCode
  # # test_IsArray_InputIsValid_ThrowsException_ReturnFalse

  # @pytest.mark.parametrize(
  #   "input",
  #   [
  #     None,
  #     "",
  #   ],
  # )
  # def test_IsDictionary_InputIsNotValid_ThrowSystemExit(
  #   self,
  #   input,
  # ):
  #   with pytest.raises(SystemExit) as contextManager:
  #     result = BashDatatype.IsDictionary(input)

  #   assert contextManager.value.code == 1

  # # test_IsDictionary_InputIsValid_ReturnCode
  # # test_IsDictionary_InputIsValid_ThrowsException_ReturnFalse

  # @pytest.mark.parametrize(
  #   "input",
  #   [
  #     None,
  #     "",
  #   ],
  # )
  # def test_IsVariable_InputIsNotValid_ThrowSystemExit(
  #   self,
  #   input,
  # ):
  #   with pytest.raises(SystemExit) as contextManager:
  #     result = BashDatatype.IsVariable(input)

  #   assert contextManager.value.code == 1

  # test_IsVariable_InputIsValid_ReturnCode
  # test_IsVariable_InputIsValid_ThrowsException_ReturnFalse

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