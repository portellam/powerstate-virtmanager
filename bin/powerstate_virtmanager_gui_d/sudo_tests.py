#!/usr/bin/env python3

#
# Filename:       sudo_tests.py
# Version:        1.0.0
# Description:    Sudo unit tests.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

import os
import pytest
import unittest
from unittest.mock  import Mock, patch

from .sudo     import Sudo

class SudoTests(unittest.TestCase):
  placeholder = ""

  @patch('os.system')
  def test_is_root_command_executes_user_is_not_root_returns_false( \
    self,
    mock_os_system
  ):
    mock_os_system.return_value = 1
    sudo = Sudo()

    result1 = sudo.is_sudo
    sudo.is_root()
    result2 = sudo.is_sudo

    assert not result1
    assert not result2

  @patch('os.system')
  def test_is_root_command_executes_user_is_root_returns_true( \
    self,
    mock_os_system
  ):
    mock_os_system.return_value = 0
    sudo = Sudo()

    result1 = sudo.is_sudo
    sudo.is_root()
    result2 = sudo.is_sudo

    assert not result1
    assert result2

if __name__ == '__main__':
  unittest.main()