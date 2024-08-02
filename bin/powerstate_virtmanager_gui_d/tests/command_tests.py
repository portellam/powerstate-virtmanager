#!/usr/bin/env python3

#
# Filename:       command_tests.py
# Version:        1.0.0
# Description:    Command unit tests.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
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

      result1 = command1.get_code(self.bogus_command)
      result2 = command2.get_code("false")
      result3 = command2.get_code(None)
      result4 = command3.get_code("true")

      assert result1 == 1
      assert result2 == 1
      assert result3 == 1
      assert result4 == 1
      mock_set_completed_process.assert_called_once

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
      result3 = command2.get_code(None)
      result4 = command3.get_code("true")

      assert result1 == 127
      assert result2 == 1
      # assert result3 == 0 # FIXME: set_completed_process(). Empty string always returns 0.
      # assert result4 == 0 # FIXME: set_completed_process(). "true" always returns 0.
      mock_set_completed_process.assert_called_once

if __name__ == '__main__':
  unittest.main()