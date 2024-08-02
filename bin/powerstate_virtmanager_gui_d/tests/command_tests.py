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

  def test_get_code_throws_exception_return_one(self):
    with patch.object( \
      Command,
      'set_completed_process'
    ) as mock_set_completed_process:
      mock_set_completed_process.side_effect = Exception(Exception)
      command1      = Command()
      command2      = Command()
      command3      = Command()
      command4      = Command()

      result1 = command1.get_code(self.bogus_command)
      result2 = command2.get_code("false")
      result3 = command3.get_code(None)
      result4 = command4.get_code("true")

      assert result1 == 1
      assert result2 == 1
      assert result3 == 1
      assert result4 == 1
      assert mock_set_completed_process.call_count == 4

  def test_get_code_succeeds_return_expected_code(self):
    with patch.object( \
      Command,
      'set_completed_process'
    ) as mock_set_completed_process:
      mock_set_completed_process.side_effect = None
      command1      = Command()
      command2      = Command()
      command3      = Command()
      command4      = Command()
      command1.code = 127
      command2.code = 1
      command3.code = 0
      command4.code = 0

      result1 = command1.get_code(self.bogus_command)
      result2 = command2.get_code("false")
      result3 = command3.get_code(None)
      result4 = command4.get_code("true")

      assert result1 == 127
      assert result2 == 1
      assert result3 == 0
      assert result4 == 0
      assert mock_set_completed_process.call_count == 4

  def test_make_command_sudo_is_sudo_is_false_return_command(self):
      command1              = Command()
      command2              = Command()
      command3              = Command()
      command1.sudo.is_sudo = False
      command2.sudo.is_sudo = False
      command3.sudo.is_sudo = False

      result1 = command1.make_command_sudo("false")
      result2 = command2.make_command_sudo(None)
      result3 = command3.make_command_sudo("true")

      assert result1 == "false"
      assert result2 == ""
      assert result3 == "true"

  def test__make_command_sudo__command_is_empty_string__always_return_empty_string(self):
    command1              = Command()
    command2              = Command()
    command3              = Command()
    command1.sudo.is_sudo = True
    command2.sudo.is_sudo = False

    result1 = command1.make_command_sudo("")
    result2 = command3.make_command_sudo("")

    assert result1 == ""
    assert result2 == ""

  def test__make_command_sudo__command_is_none__always_return_empty_string(self):
    command1              = Command()
    command2              = Command()
    command3              = Command()
    command1.sudo.is_sudo = True
    command2.sudo.is_sudo = False

    result1 = command1.make_command_sudo(None)
    result2 = command3.make_command_sudo(None)

    assert result1 == ""
    assert result2 == ""

  def test__make_command_sudo__command_is_valid__is_sudo_is_true__return_sudo_command(self):
    command1              = Command()
    command2              = Command()
    command3              = Command()
    command1.sudo.is_sudo = True
    command2.sudo.is_sudo = True
    command3.sudo.is_sudo = True

    result1 = command1.make_command_sudo("false")
    result2 = command3.make_command_sudo("true")

    assert result1 == "sudo false"
    assert result2 == "sudo true"

if __name__ == '__main__':
  unittest.main()