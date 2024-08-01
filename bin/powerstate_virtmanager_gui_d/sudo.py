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
    self.is_sudo = False

  def set_is_sudo(self):
    command = "[ $( whoami ) == \"root\" ]"
    result = os.system(command) == 0
    self.is_sudo = result