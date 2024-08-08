#!/usr/bin/env python3

#
# Filename:       domain_tests.py
# Version:        1.0.0
# Description:    Domain unit tests.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

# TODO: add enum for multiple dependencies.

import unittest
from unittest.mock  import patch

from ..command  import Command
from ..domain   import Domain

class DomainTests(unittest.TestCase):
  placeholder = ""

  def test__does_dependency_exist(self):
    dependency = "virsh"
    check_dependency = "command -v {}".format(dependency)
    command = Command(check_dependency)

    try:
      command.run()
      is_available = command.code == 0

    except:
      print("Could not determine if dependency '{}' exists.".format(dependency))
      assert False

    if not is_available:
      print("Dependency '{}' is not available.".format(dependency))
      assert False

    print("Dependency '{}' is available.".format(dependency))
    assert True

if __name__ == '__main__':
  unittest.main()