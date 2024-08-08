#!/usr/bin/env python3

#
# Filename:       command_tests.py
# Version:        1.0.0
# Description:    Command unit tests.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

import unittest
from unittest.mock  import patch

from ..command  import Command

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
    command = Command("echo \"Hello\nWorld\"")
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
    command = Command("echo \"Hello\nWorld\"")
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
    command = Command("echo \"Hello\nWorld\"")
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
    command = Command("sudo echo \"Hello\nWorld\"")
    command.sudo.is_sudo = True

    command.make_sudo()
    result = command.command

    assert result == "sudo echo \"Hello\nWorld\""

  def test__make_sudo__is_sudo__command_is_none__command_is_empty_string(self):
    command = Command(None)
    command.sudo.is_sudo = True

    command.make_sudo()
    result = command.command

    assert result == ""

  def test__make_sudo__is_sudo__command_is_valid__command_has_sudo_prefix(self):
    command = Command("echo \"Hello\nWorld\"")
    command.sudo.is_sudo = True

    command.make_sudo()
    result = command.command

    assert result == "sudo echo \"Hello\nWorld\""

  def test__make_sudo__is_not_sudo__command_is_valid__command_is_unchanged(self):
    command = Command("echo \"Hello\nWorld\"")
    command.sudo.is_sudo = False

    command.make_sudo()
    result = command.command

    assert result == "echo \"Hello\nWorld\""

  @patch('subprocess.run')
  def test__run__use_sudo_if_available_is_false_command_is_not_valid_and_fails__throws_exception( \
    self,
    mock_subprocess_run
  ):
    mock_subprocess_run.raises(Exception)

    with self.assertRaises(Exception):
      command = Command(self.bogus_command)
      command.use_sudo_if_available = False

      command.run()
      result_code     = command.code
      result_command  = command.command
      result_error    = command.error
      result_output   = command.output

      mock_subprocess_run.assert_called_once()
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

    assert result_command == "false"
    assert result_code    == 1
    assert result_error   == ""
    assert result_output  == ""

  def test__run__use_sudo_if_available_is_false__command_is_valid_and_runs_and_passes(self):
    command = Command("echo \"Hello\nWorld\"")
    command.use_sudo_if_available = False

    command.run()
    result_code     = command.code
    result_command  = command.command
    result_error    = command.error
    result_output   = command.output

    assert result_command == "echo \"Hello\nWorld\""
    assert result_code    == 0
    assert result_error   == ""
    assert result_output  == "Hello\nWorld\n"

  def test__run__use_sudo_if_available_is_true__command_is_valid_and_runs_and_passes(self):
    command = Command("echo \"Hello\nWorld\"")
    command.use_sudo_if_available = True

    command.run()
    result_code     = command.code
    result_command  = command.command
    result_error    = command.error
    result_output   = command.output

    assert result_command == "sudo echo \"Hello\nWorld\""
    assert result_code    == 0
    assert result_error   == ""
    assert result_output  == "Hello\nWorld\n"

if __name__ == '__main__':
  unittest.main()