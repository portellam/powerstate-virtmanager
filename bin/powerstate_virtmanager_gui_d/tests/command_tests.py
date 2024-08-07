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
  command       = None
  bogus_command = "this_command_should_not_exist_in_bash"

  def setUp(self):
    self.command = Command()

  def test__get_output_as_string__command_is_empty_string__return_empty_string(self):
    self.command.command = ""

    result = self.command.get_output_as_string()

    assert result == ""

  def test__get_output_as_string__command_is_none__return_empty_string(self):
    self.command.command = None

    result = self.command.get_output_as_string()

    assert result == ""

  def test__get_output_as_list__command_fails__return_empty_list(self):
    self.command = Command("echo -e \"Hello\nWorld\"")
    self.command.code = 1
    self.command.error = "this_is_an_error"

    self.command.output = [
      "Hello",
      "World"
    ]

    result = self.command.get_output_as_list()

    assert result != [
      "Hello",
      "World"
    ]

    assert result == []

  def test__get_output_as_list__command_passes__return_list(self):
    self.command = Command("echo -e \"Hello\nWorld\"")
    self.command.code = 0
    self.command.error = "this_is_an_error"

    self.command.output = [
      "Hello",
      "World"
    ]

    result = self.command.get_output_as_list()

    assert result != []

    assert result == [
      "Hello",
      "World"
    ]

  def test__get_output_as_list__command_is_none__return_empty_list(self):
    self.command = Command("echo -e \"Hello\nWorld\"")
    self.command.code = 127
    self.command.error = "this_is_an_error"

    self.command.output = [
      "Hello",
      "World"
    ]

    result = self.command.get_output_as_list()

    assert result != [
      "Hello",
      "World"
    ]

    assert result == []

  def test__get_output_as_string__command_fails__return_empty_string(self):
    self.command = Command("echo -e \"Hello\nWorld\"")
    self.command.code = 1
    self.command.error = "this_is_an_error"

    self.command.output = [
      "Hello",
      "World"
    ]

    result = self.command.get_output_as_string()

    assert result != "Hello World"
    assert result == ""

  def test__get_output_as_string__command_passes__return_delimited_output(self):
    self.command = Command("echo -e \"Hello\nWorld\"")
    self.command.code = 0
    self.command.error = "this_is_an_error"

    self.command.output = [
      "Hello",
      "World"
    ]

    result = self.command.get_output_as_string()

    assert result != ""
    assert result == "Hello World"

  def test__get_output_as_string__command_is_none__return_empty_string(self):
    self.command = Command(None)
    self.command.code = 127
    self.command.error = "this_is_an_error"

    self.command.output = [
      "Hello",
      "World"
    ]

    result = self.command.get_output_as_string()

    assert result != "Hello World"
    assert result == ""

if __name__ == '__main__':
  unittest.main()