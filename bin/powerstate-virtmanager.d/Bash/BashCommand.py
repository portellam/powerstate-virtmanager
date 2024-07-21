#!/usr/local/bin/python

#
# Filename:       BashCommand.py
# Version:        1.0.0
# Description:    Bash command input and output logic.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

import os
import subprocess
import sys

class BashCommand:
  def GetCommandInput():
    try:
      result = sys.stdin.readline()
      return result

    except Exception exception:
      print(exception)
      sys.exit(1)

  def GetCommandOutput(command):
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

  def GetCommandReturnCode(command):
    if command is None:
      sys.exit(1)

    try:
      return os.system(command)

    except subprocess.CalledProcessError:
      print(exception)
      sys.exit(1)