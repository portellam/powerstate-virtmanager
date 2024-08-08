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
import traceback

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

    if self.command == [] \
      or self.command == [ None ]:
      self.command = [ "" ]
      return

    is_list = len(self.command) > 1

    if self.command == "" \
      or not self.sudo.is_sudo:
      return

    if is_list \
      and self.command[0] == Sudo.command:
      return

    if not is_list \
      and self.command.startswith(Sudo.command):
      return

    if not is_list:
      self.command = "{} {}".format( \
        Sudo.command,
        self.command
      )

      return

    self.command.insert(0, Sudo.command)

  def run(self):
    if self.use_sudo_if_available:
      self.make_sudo()

    result = None

    try:
      result = subprocess.run(
        args            = self.command,
        capture_output  = True,
        shell           = True
      )

    except Exception:
      self.code = self.fail_code
      traceback.print_exc()
      raise

    self.code   = result.returncode
    self.error  = result.stderr.decode('ascii')
    self.output = result.stdout.decode('ascii')
