#!/usr/bin/env python3

#
# Filename:       command.py
# Version:        1.0.0
# Description:    Bash command logic.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

#
# TODO:
# - [ ] gracefully fail if you cannot parse info for one domain.
# - [ ] add unit tests.
#

import subprocess
import sys

from .sudo import Sudo

class Command:
  sudo      = Sudo
  code      = 127   # the return code for an non-existing command.
  fail_code = 1
  error     = ""
  output    = ""

  def __init__(self):
    self.sudo     = Sudo
    self.sudo.set_is_sudo(self)

    self.code     = 127   # the return code for an non-existing command.
    self.stderr   = ""
    self.stdout   = ""

  def make_command_sudo( \
    self,
    command
  ):
    if not self.sudo.is_sudo:
      return command

    command = "{} {}".format( \
      Sudo.command,
      command
    )

    return command

  def set_completed_process( \
    self,
    command
  ):
    try:
      result = subprocess.run(
        args            = self.make_command_sudo(command),
        capture_output  = True,
      )

    except Exception as contextManager:
      print(contextManager.exception.output)
      self.code = fail_code
      raise

    self.code   = result.returncode
    self.error  = result.stderr.decode('ascii')
    self.output = result.stdout.decode('ascii')

  def get_code( \
    self,
    command
  ):
    try:
      self.set_completed_process(command)

    except:
      return 1

    return self.code

  def get_output_as_list( \
    self,
    command
  ):
    try:
      self.set_completed_process(command)

    except:
      sys.exit(1)

    if self.code != 0:
      print(self.error.splitlines())
      sys.exit(1)

    return self.output.splitlines()

  def get_output_as_string( \
    self,
    command
  ):
    try:
      self.set_completed_process(command)

    except:
      sys.exit(1)

    if self.code != 0:
      print(self.error.splitlines())
      sys.exit(1)

    return self.output.splitlines()[0]