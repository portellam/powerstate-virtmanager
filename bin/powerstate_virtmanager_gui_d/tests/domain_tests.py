#!/usr/bin/env python3

#
# Filename:       domain_tests.py
# Version:        1.0.0
# Description:    Domain unit tests.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

#
# TODO:
# - [ ] add enum for multiple dependencies?
# - [x] test domain xml?
#    - [ ] disable libvirt hooks for these domains? It's a user permissions issue.
#
#

import os
import unittest
from unittest.mock  import patch

from ..domain   import Domain

class DomainTests(unittest.TestCase):
  test_data_directory='domain_tests_data'
  test_kvm_domain_path='./{}/kvm-example.xml'.format(test_data_directory)

  def setUp(self):
    self.setUp__create_domain(self.test_kvm_domain_path)

  def teardown(self):
    self.teardown__destroy_domain(self.test_kvm_domain_path)

  def setUp__create_domain(domain):
    try:
      result = os.system('virsh create '.format(domain))
      return result == 0

    except:
      print("Failed to create test domain '{}'".format(domain))
      raise

  def teardown__destroy_domain(domain):
    try:
      result = os.system('virsh destroy '.format(domain))
      return result == 0

    except:
      print("Failed to destroy test domain '{}'".format(domain))
      raise

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

  def test__does_dependency_file_exist(self):
    assert False

if __name__ == '__main__':
  unittest.main()