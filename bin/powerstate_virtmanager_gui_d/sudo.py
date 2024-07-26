#!/usr/local/bin/python

#
# Filename:       sudo.py
# Version:        1.0.0
# Description:    Determine if the Python script was executed by a sudo user.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

from bash_command import BashCommand

class Sudo:
  is_sudo = false
  command = "sudo"

  def __init__():
    self.is_sudo = BashCommand.GetCode(command) == 0