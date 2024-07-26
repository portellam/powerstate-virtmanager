#!/usr/local/bin/python

#
# Filename:       bash_datatype_tests.py
# Version:        1.0.0
# Description:    BashDatatype Unit Tests.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

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
    bashDatatype = BashDatatype()
    result = bashDatatype.IsReferenceLegal(input)
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
    bashDatatype = BashDatatype()
    result = bashDatatype.IsReferenceLegal(input)
    assert result == False

  @pytest.mark.parametrize(
    "input",
    [
      None,
      "",
    ],
  )
  def test_GetFormattedArray_InputIsNotValid_DoSystemExit(
    self,
    input,
  ):
    bashDatatype = BashDatatype()

    with pytest.raises(SystemExit) as contextManager:
      result = bashDatatype.GetFormattedArray(input)

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
    expected,
  ):
    bashDatatype = BashDatatype()
    result = bashDatatype.GetFormattedArray(input)
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
    input,
  ):
    bashDatatype = BashDatatype()

    with pytest.raises(SystemExit) as contextManager:
      result = bashDatatype.GetFormattedArrayLength(input)

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
    expected,
  ):
    bashDatatype = BashDatatype()
    result = bashDatatype.GetFormattedArrayLength(input)
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
    input,
  ):
    bashDatatype = BashDatatype()

    with pytest.raises(SystemExit) as contextManager:
      result = bashDatatype.GetFormattedKeys(input)

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
    expected,
  ):
    bashDatatype = BashDatatype()
    result = bashDatatype.GetFormattedKeys(input)
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
    input,
  ):
    bashDatatype = BashDatatype()

    with pytest.raises(SystemExit) as contextManager:
      result = bashDatatype.GetFormattedVariable(input)

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
    expected,
  ):
    bashDatatype = BashDatatype()
    result = bashDatatype.GetFormattedVariable(input)
    assert result == expected

  @pytest.mark.parametrize(
    "input",
    [
      None,
      "",
    ],
  )
  def test_GetKeysOutput_InputIsNotValid_ThrowSystemExit(
    self,
    input,
  ):
    bashDatatype = BashDatatype()

    with pytest.raises(SystemExit) as contextManager:
      result = bashDatatype.GetKeysOutput(input)

    assert contextManager.value.code == 1

  # test_GetKeysOutput_InputIsValid_ReturnOutput                                      # TODO

  @pytest.mark.parametrize(
    "input",
    [
      None,
      "",
    ],
  )
  def test_GetVariableOutput_InputIsNotValid_ThrowSystemExit(
    self,
    input,
  ):
    bashDatatype = BashDatatype()

    with pytest.raises(SystemExit) as contextManager:
      result = bashDatatype.GetVariableOutput(input)

    assert contextManager.value.code == 1

  # test_GetVariableOutput_InputIsValid_ReturnOutput                                  # TODO

  @pytest.mark.parametrize(
    "input",
    [
      None,
      "",
    ],
  )
  def test_GetStringLiteral_InputIsNullOrEmptyString_ReturnEmptyString(
    self,
    input,
  ):
    expected = "\"\""
    bashDatatype = BashDatatype()
    result = bashDatatype.GetStringLiteral(input)
    assert result == expected

  @pytest.mark.parametrize(
    "input, expected",
    [
      ( "hello", "\"hello\"" ),
      ( "world", "\"world\"" ),
    ],
  )
  def test_GetStringLiteral_InputIsNonEmptyString_ReturnString(
    self,
    input,
    expected,
  ):
    bashDatatype = BashDatatype()
    result = bashDatatype.GetStringLiteral(input)
    assert result == expected

  @pytest.mark.parametrize(
    "input",
    [
      None,
      "",
    ],
  )
  def test_IsArray_InputIsNotValid_ThrowSystemExit(
    self,
    input,
  ):
    bashDatatype = BashDatatype()

    with pytest.raises(SystemExit) as contextManager:
      result = bashDatatype.IsArray(input)

    assert contextManager.value.code == 1

  # test_IsArray_InputIsValid_ReturnCode                                              # TODO
  # test_IsArray_InputIsValid_ThrowsException_ReturnFalse                             # TODO

  @pytest.mark.parametrize(
    "input",
    [
      None,
      "",
    ],
  )
  def test_IsDictionary_InputIsNotValid_ThrowSystemExit(
    self,
    input,
  ):
    bashDatatype = BashDatatype()

    with pytest.raises(SystemExit) as contextManager:
      result = bashDatatype.IsDictionary(input)

    assert contextManager.value.code == 1

  # test_IsDictionary_InputIsValid_ReturnCode                                         # TODO
  # test_IsDictionary_InputIsValid_ThrowsException_ReturnFalse                        # TODO

  @pytest.mark.parametrize(
    "input",
    [
      None,
      "",
    ],
  )
  def test_IsVariable_InputIsNotValid_ThrowSystemExit(
    self,
    input,
  ):
    bashDatatype = BashDatatype()

    with pytest.raises(SystemExit) as contextManager:
      result = bashDatatype.IsVariable(input)

    assert contextManager.value.code == 1

  # test_IsVariable_InputIsValid_RunCommandFails_ReturnFalse                          # TODO

  # @patch('bash_command.BashCommand')
  # def test_IsVariable_InputIsValid_VariableDoesExist_ReturnFalse( \                 # FIXME
  #   self,
  #   mock_BashCommand
  # ):
  #   mock_BashCommand.code = 0
  #   bashDatatype = BashDatatype()
  #   result = bashDatatype.IsVariable("var")
  #   assert result == True
  #   mock_BashCommand.assert_called_once()

  # @patch('bash_command.BashCommand')
  # def test_IsVariable_InputIsValid_VariableDoesNotExist_ReturnFalse( \              # FIXME
  #   self,
  #   mock_BashCommand
  # ):
  #   mock_BashCommand.code = 127
  #   bashDatatype = BashDatatype()
  #   result = bashDatatype.IsVariable("var")
  #   assert result == False
  #   mock_BashCommand.assert_called_once()

if __name__ == '__main__':
  unittest.main()