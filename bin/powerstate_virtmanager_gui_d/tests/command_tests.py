#!/usr/bin/env python3

#
# Filename:       command_tests.py
# Version:        1.0.0
# Description:    Command unit tests.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

#
# NOTES:
# - cannot use parameters with self as input.
#
#

import pytest
import unittest
from unittest.mock  import Mock, patch

from ..command  import Command
from ..sudo     import Sudo

class CommandTests(unittest.TestCase):
  bogus_command = "this_command_should_not_exist_in_bash"


  def test__get_output_as_string__command_is_empty_string__return_empty_string(self):
    command = Command("")

    result = command.get_output_as_string()

    assert result == ""

  def test__get_output_as_string__command_is_none__return_empty_string(self):
    command = Command(None)

    result = command.get_output_as_string()

    assert result == ""

  def test__get_output_as_list__command_fails__return_empty_list(self):
    command = Command(self.bogus_command)
    command.code = 1
    command.error = "this_is_an_error"

    command.output = [
      "Hello",
      "World"
    ]

    result = command.get_output_as_list()

    assert result != [
      "Hello",
      "World"
    ]

    assert result == []

  def test__get_output_as_list__command_passes__return_list(self):
    command = Command("echo -e \"Hello\nWorld\"")
    command.code = 0
    command.error = "this_is_an_error"

    command.output = [
      "Hello",
      "World"
    ]

    result = command.get_output_as_list()

    assert result != []

    assert result == [
      "Hello",
      "World"
    ]

  def test__get_output_as_list__command_is_none__return_empty_list(self):
    command = Command("echo -e \"Hello\nWorld\"")
    command.code = 127
    command.error = "this_is_an_error"

    command.output = [
      "Hello",
      "World"
    ]

    result = command.get_output_as_list()

    assert result != [
      "Hello",
      "World"
    ]

    assert result == []

  def test__get_output_as_string__command_fails__return_empty_string(self):
    command = Command(self.bogus_command)
    command.code = 1
    command.error = "this_is_an_error"

    command.output = [
      "Hello",
      "World"
    ]

    result = command.get_output_as_string()

    assert result != "Hello World"
    assert result == ""

  def test__get_output_as_string__command_passes__return_delimited_output(self):
    command = Command("echo -e \"Hello\nWorld\"")
    command.code = 0
    command.error = "this_is_an_error"

    command.output = [
      "Hello",
      "World"
    ]

    result = command.get_output_as_string()

    assert result != ""
    assert result == "Hello World"

  def test__get_output_as_string__command_is_none__return_empty_string(self):
    command = Command(None)
    command.code = 127
    command.error = "this_is_an_error"

    command.output = [
      "Hello",
      "World"
    ]

    result = command.get_output_as_string()

    assert result != "Hello World"
    assert result == ""

  def test__make_sudo__command_has_sudo_prefix__command_is_unchanged(self):
    command = Command("sudo echo -e \"Hello\nWorld\"")
    command.sudo.is_sudo = True

    command.make_sudo()
    result = command.command

    assert result == "sudo echo -e \"Hello\nWorld\""

  def test__make_sudo__is_sudo__command_is_none__command_is_empty_string(self):
    command = Command(None)
    command.sudo.is_sudo = True

    command.make_sudo()
    result = command.command

    assert result == ""

  def test__make_sudo__is_sudo__command_is_valid__command_has_sudo_prefix(self):
    command = Command("echo -e \"Hello\nWorld\"")
    command.sudo.is_sudo = True

    command.make_sudo()
    result = command.command

    assert result == "sudo echo -e \"Hello\nWorld\""

  def test__make_sudo__is_not_sudo__command_is_valid__command_is_unchanged(self):
    command = Command("echo -e \"Hello\nWorld\"")
    command.sudo.is_sudo = False

    command.make_sudo()
    result = command.command

    assert result == "echo -e \"Hello\nWorld\""

  def test__run__use_sudo_if_available_is_false_command_is_not_valid_and_fails__throws_exception(self):
    with self.assertRaises(Exception) as contextManager:
      command = Command(self.bogus_command)
      command.use_sudo_if_available = False

      command.run()
      result_code     = command.code
      result_command  = command.command
      result_error    = command.error
      result_output   = command.output

      assert result_command == self.bogus_command
      assert result_code    == 1
      assert result_error   == ""
      assert result_output  == ""

  def test__run__use_sudo_if_available_is_false_command_is_valid_and_fails(self):
    command = Command("false")
    command.use_sudo_if_available = False

    command.run()
    result_code     = command.code
    result_command  = command.command
    result_error    = command.error
    result_output   = command.output

    self.assertRaises(Exception, command)
    assert result_command == "false"
    assert result_code    == 1
    assert result_error   == ""
    assert result_output  == ""

  def test__run__use_sudo_if_available_is_false_command_is_valid_and_runs_and_passes(self):
    command = Command("echo -e \"Hello\nWorld\"")
    command.use_sudo_if_available = False

    command.run()
    result_code     = command.code
    result_command  = command.command
    result_error    = command.error
    result_output   = command.output

    expected_output = [
      "Hello"
      "World"
    ]

    assert result_command == "echo -e \"Hello\nWorld\""
    assert result_code    == 1
    assert result_error   == ""
    assert result_output  == expected_output

  def test__run__use_sudo_if_available_is_true__command_is_valid_and_runs_and_passes(self):
    command = Command("echo -e \"Hello\nWorld\"")
    command.use_sudo_if_available = True

    command.run()
    result_code     = command.code
    result_command  = command.command
    result_error    = command.error
    result_output   = command.output

    expected_output = [
      "Hello"
      "World"
    ]

    assert result_command == "sudo echo -e \"Hello\nWorld\""
    assert result_code    == 0
    assert result_error   == ""
    assert result_output  == expected_output

if __name__ == '__main__':
  unittest.main()