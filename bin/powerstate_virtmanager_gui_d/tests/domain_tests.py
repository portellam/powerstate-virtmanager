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

  test_domain_name_list = [
    'kvm-example'
  ]

  def setUp(self):
    for domain in self.test_domain_name_list:
      path = './{}/{}.xml'.format( \
        self.test_data_directory,
        domain
      )

      self.setUp__create_domain(path)

  def teardown(self):
    for domain in self.test_domain_name_list:
      self.teardown__destroy_domain(domain)

  def setUp__create_domain( \
    self,
    domain
  ):
    try:
      result = os.system('virsh create --file {}'.format(domain))
      return result == 0

    except:
      print("Failed to create test domain '{}'".format(domain))
      raise

  def teardown__destroy_domain( \
    self,
    domain
  ):
    try:
      result = os.system('virsh destroy {}'.format(domain))
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

  def test__does_test_data_exist(self):
    for domain in self.test_domain_name_list:
      path = './{}/{}.xml'.format( \
        self.test_data_directory,
        domain
      )

      if not os.path.isfile(path):
        print("Test domain file '{}' does not exist.".format(path))
        assert False

    print("All test domain files exist.")
    assert True

  def test__reset__is_running__set_power_state_is_called(self):
    domain = Domain(self.test_domain_name_list[0])

    try:
      domain.reset()

      result = domain.power_state

      assert result != "running"

    except:
      assert False

if __name__ == '__main__':
  unittest.main()