#!/usr/bin/env python3

#
# Filename:       sudo_tests.py
# Version:        1.0.0
# Description:    Sudo unit tests.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

import pytest
import unittest
from unittest.mock  import Mock, patch

from ..sudo     import Sudo

@patch('os.system')
class SudoTests(unittest.TestCase):
  def test_set_is_sudo_command_executes_user_is_not_root_returns_false( \
    self,
    mock_os_system
  ):
    mock_os_system.return_value = 1
    sudo = Sudo()

    result1 = sudo.is_sudo
    sudo.set_is_sudo()
    result2 = sudo.is_sudo

    assert not result1
    assert not result2

  def test_set_is_sudo_command_executes_user_set_is_sudo_returns_true( \
    self,
    mock_os_system
  ):
    mock_os_system.return_value = 0
    sudo = Sudo()

    result1 = sudo.is_sudo
    sudo.set_is_sudo()
    result2 = sudo.is_sudo

    assert not result1
    assert result2

if __name__ == '__main__':
  unittest.main()