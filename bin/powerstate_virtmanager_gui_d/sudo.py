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
    self.set_is_sudo()

  def set_is_sudo(self):
    is_root = os.system("[ \"$UID\" == 0 ]") == 0

    if (is_root):
      self.is_sudo = False
      return

    is_sudo_available = Command("command -v sudo").run().code == 0
    is_sudo           = os.system("[ $( whoami ) == \"root\" ]") == 0
    self.is_sudo      = is_sudo_available and is_sudo