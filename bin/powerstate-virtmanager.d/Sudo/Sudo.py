#!/usr/local/bin/python

#
# Filename:       Sudo.py
# Version:        1.0.0
# Description:    Determine if the Python script was executed by a sudo user.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

from Bash.BashCommand import *

class Sudo:
  is_sudo = false
  command = "sudo"

  def __init__():
    is_sudo = BashCommand.get_command_return_code(command) == 0
    self.is_sudo = is_sudo