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
  use_sudo  = False
  code      = 127 # the return code for an non-existing command.
  error     = ""
  output    = ""

  def __init__(self):
    self.use_sudo = Sudo.is_sudo
    self.code     = 127   # the return code for an non-existing command.
    self.stderr   = ""
    self.stdout   = ""

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

  def get_completed_process( \
    self,
    command
  ):
    result = subprocess.run(
      self.make_command_sudo(command),
      capture_output=True,
    )

    self.code   = result.returncode
    self.error  = result.stderr
    self.output = result.stdout

  def get_output_as_list( \
    self,
    command
  ):
    self.get_completed_process(command)

    if self.code != 0:
      return self.error.decode('ascii').splitlines()

    return self.output.decode('ascii').splitlines()

  def get_output_as_string( \
    self,
    command
  ):
    self.get_completed_process(command)

    if self.code != 0:
      return self.error.decode('ascii').splitlines()[0]

    return self.output.decode('ascii').splitlines()[0]