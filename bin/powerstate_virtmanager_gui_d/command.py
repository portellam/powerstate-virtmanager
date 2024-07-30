#!/usr/bin/env python

#
# Filename:       command.py
# Version:        1.0.0
# Description:    
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

import subprocess
from sudo import Sudo

class Command:
  use_sudo = False

  def __init__(self):
    self.use_sudo = Sudo.is_sudo

  def make_command_sudo( \
    self,
    command
  ):
    if not self.use_sudo:
      return command

    command = "{} {}".format( \
      Sudo.command,
      command
    )

  def get_stdout_as_list( \
    self,
    command
  ):
    return subprocess.run(
      self.make_command_sudo(command),
      capture_output=True,
    ).decode('ascii') \
    .splitlines()

  def get_stdout_as_string( \
    self,
    command
  ):
    return self.get_stdout_as_list(command)[0]