#!/usr/local/bin/python

#
# Filename:       BashDatatypeTests.py
# Version:        1.0.0
# Description:    BashDatatype Unit Tests.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

import subprocess
import sys
import unittest
from unittest.mock      import patch
from unittest.mock      import Mock
from Bash.BashDatatype  import BashDatatype

class BashCommandTests(unittest.TestCase):
  def test_GetStringLiteral_ReturnString(self):
    expected1 = "\"\""
    expected2 = "\"\""
    expected3 = "\"hello\""

    result1 = BashDatatype.GetStringLiteral(None)
    result2 = BashDatatype.GetStringLiteral("")
    result3 = BashDatatype.GetStringLiteral("hello")

    self.assertEqual(expected1, result1)
    self.assertEqual(expected2, result2)
    self.assertEqual(expected3, result3)

if __name__ == '__main__':
  unittest.main()