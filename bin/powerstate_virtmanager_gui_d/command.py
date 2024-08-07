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

from .sudo import Sudo

class Command:
  code                  = None
  command               = ""
  error                 = ""
  output                = ""
  use_sudo_if_available = False

  fail_code = 1
  sudo      = None

  def __init__( \
    self,
    command               = "",
    use_sudo_if_available = False
  ):
    self.sudo = Sudo
    self.sudo.set_is_sudo(self)

    if (command == None):
      command = ""

    self.command                = command
    self.code                   = 127
    self.error                  = ""
    self.output                 = ""
    self.use_sudo_if_available  = use_sudo_if_available

  def get_output_as_list(self):
    if self.command is None:
      return []

    if self.code != 0:
      print(self.error)
      return []

    return self.output

  def get_output_as_string(self):
    if self.command is None \
      or self.command == "":
      return ""

    if self.code != 0:
      print(self.error)
      return ""

    if len(self.output) > 2:
      return self.output

    delimiter = ' '
    return delimiter.join(self.output)

  def make_sudo(self):
    if self.command is None:
      self.command == ""
      return

    if self.command == "" \
      or not self.sudo.is_sudo \
      or self.command.startswith(Sudo.command):
      return

    self.command = "{} {}".format( \
      Sudo.command,
      self.command
    )

  def run(self):
    if self.use_sudo_if_available:
      self.make_sudo()

    try:
      result = subprocess.run(
        args            = self.command,
        capture_output  = True,
      )

    except Exception as contextManager:
      print(contextManager.exception.output)
      self.code = self.fail_code
      raise

    self.code   = result.returncode
    self.error  = result.stderr.decode('ascii')
    self.output = result.stdout.decode('ascii')
