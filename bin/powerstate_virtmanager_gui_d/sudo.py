#!/usr/bin/env python3

#
# Filename:       sudo.py
# Version:        1.0.0
# Description:    Determine if the Python script was executed by a sudo user.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

import os

class Sudo:
  is_sudo = False
  command = "sudo"

  def __init__(self):
    self.is_sudo = self.is_sudo() and not self.is_root()

  def is_sudo(self):
    is_sudo_available = os.system("command -v sudo") == 0
    is_sudo           = os.system("[ $( whoami ) == \"root\" ]") == 0
    return is_sudo_available and is_sudo

  def is_root(self):
    return os.system("[ \"$UID\" == 0 ]") == 0