#!/usr/local/bin/python

#
# Filename:       BashCommand.py
# Version:        1.0.0
# Description:    Bash command input and output logic.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

import subprocess
import sys

class BashCommand:
  code = 127
  command = None
  output = None

  def __init__(self, command):
    self.code = 127
    self.command = command
    self.output = ""

  def GetInput(self):
    return sys.stdin.readline()

  def RunCommand(self):
    if command is None:
      __init__()

    try:
      result = subprocess.run(
        command,
        capture_output = True,  # Python >= 3.7 only
        text = True             # Python >= 3.7 only
      )

      code = result.return_code
      output = result.stdout

    except:
      __init__(command)

  def SetInput():
    try:
      code = 127
      output = GetInput()
      command = ""

    except:
      output = None
      command = None