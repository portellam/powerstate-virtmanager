#!/usr/bin/env python3

#
# Filename:       sudo_tests.py
# Version:        1.0.0
# Description:    Sudo unit tests.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

import os
import sys
import unittest

if sys.version_info >= (3, 3):
    from unittest.mock  import MagicMock, patch
else:
    from mock           import MagicMock, patch

from ..sudo         import Sudo

class SudoTests(unittest.TestCase):
  def test__does_dependency_exist(self):
    dependency = "sudo"
    check_dependency = "command -v {}".format(dependency)
    is_available = False

    try:
      is_available = os.system(check_dependency) == 0

    except:
      print("Could not determine if dependency '{}' exists.".format(dependency))
      assert False

    if not is_available:
      print("Dependency '{}' is not available.".format(dependency))
      assert False

    print("Dependency '{}' is available.".format(dependency))
    assert True

  @patch('os.system')
  def test__is_root__os_system_fails__returns_false( \
    self,
    mock_system
  ):
    mock_system.return_value = 1

    result = Sudo.is_root(self)

    assert mock_system.call_count == 1
    assert not result

  @patch('os.system')
  def test__is_root__os_system_passes__returns_true( \
    self,
    mock_system
  ):
    mock_system.return_value = 0

    result = Sudo.is_root(self)

    assert mock_system.call_count == 1
    assert result

  @patch('os.system')
  def test__is_sudo__os_system_fails__returns_false( \
    self,
    mock_system
  ):
    mock_system.return_value = 1

    result = Sudo.is_sudo(self)

    assert mock_system.call_count == 2
    assert not result

  @patch('os.system')
  def test__is_sudo__os_system_passes__returns_true( \
    self,
    mock_system
  ):
    mock_system.return_value = 0

    result = Sudo.is_sudo(self)

    assert mock_system.call_count == 2
    assert result

if __name__ == '__main__':
  unittest.main()