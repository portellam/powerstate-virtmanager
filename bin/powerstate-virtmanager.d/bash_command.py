#!/usr/local/bin/python

#
# Filename:       bash_command.py
# Version:        1.0.0
# Description:    Bash command input and output logic.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

import subprocess
import sys

class bash:
  def get_command_input():
    try:
      result = sys.stdin.readline()
      return result

    except subprocess.CalledProcessError as exception:
        print(exception)
        sys.exit(1)

  def get_command_output(command):
    if command is None:
      sys.exit(1)

    try:
        result = subprocess.check_output(
          command,
          shell = True,
          stderr = subprocess.STDOUT,
          text = True
        )

        return result

    except subprocess.CalledProcessError as exception:
        print(exception)
        sys.exit(1)