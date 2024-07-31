#!/usr/bin/env python3

#
# Filename:       domain_list_tests.py
# Version:        1.0.0
# Description:    DomainList unit tests.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

import pytest
import unittest
from unittest.mock  import Mock, patch

from .command      import Command
from .domain       import Domain
from .domain_list  import DomainList

class DomainListTests(unittest.TestCase):
  placeholder = ""

if __name__ == '__main__':
  unittest.main()