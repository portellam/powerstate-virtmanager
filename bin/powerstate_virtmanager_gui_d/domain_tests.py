#!/usr/bin/env python3

#
# Filename:       domain_tests.py
# Version:        1.0.0
# Description:    Domain unit tests.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

import pytest
import unittest
from unittest.mock  import Mock, patch

from .command  import Command
from .domain   import Domain

class DomainTests(unittest.TestCase):
  placeholder = ""

if __name__ == '__main__':
  unittest.main()