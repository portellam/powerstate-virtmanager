#!/usr/bin/env python3

#
# Filename:       domain_tests.py
# Version:        1.0.0
# Description:    Domain unit tests.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

# TODO: add enum for multiple dependencies?

import os
import unittest
from unittest.mock  import patch

from ..domain   import Domain

class DomainTests(unittest.TestCase):
  def test__does_dependency_exist(self):
    dependency = "virsh"
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

if __name__ == '__main__':
  unittest.main()