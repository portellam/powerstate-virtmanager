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

class BashCommand(object):
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
    if self.command is None:
      self.__init__()

    try:
      result = subprocess.run(
        self.command,
        capture_output = True,  # Python >= 3.7 only
        text = True             # Python >= 3.7 only
      )

      self.code = result.return_code
      self.output = result.stdout

    except:
      self.__init__(command)

  def SetInput(self):
    try:
      self.code = 127
      self.output = self.GetInput()
      self.command = ""

    except:
      self.output = None
      self.command = None