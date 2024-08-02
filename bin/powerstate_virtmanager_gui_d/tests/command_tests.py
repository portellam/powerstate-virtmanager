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
  placeholder = ""

  def test_get_code_throws_exception_return_one(self):
    with patch.object(Command, 'set_completed_process') as \
      mock_set_completed_process:

      mock_set_completed_process.side_effect = Exception(Exception)

    result1 = Command.get_code(self, None)
    result2 = Command.get_code(self, "")
    result3 = Command.get_code(self, "echo 419")

    assert result1 == 1
    assert result2 == 1
    assert result3 == 1

    mock_set_completed_process.assert_called_once

if __name__ == '__main__':
  unittest.main()