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

if __name__ == '__main__':
  unittest.main()