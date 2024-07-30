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

import os

from sudo     import Sudo

class SudoTests(unittest.TestCase):
  placeholder = ""

if __name__ == '__main__':
  unittest.main()