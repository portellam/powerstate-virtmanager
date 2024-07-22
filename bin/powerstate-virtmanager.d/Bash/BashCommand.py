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
  def GetInput():
    try:
      result = sys.stdin.readline()
      return result

    except Exception as contextManager:
      print(exception)
      sys.exit(1)

  def GetOutput(command):
    if command is None:
      return None

    try:
      result = subprocess.run(command)
      return result.output

    except:
      return ""

  def GetCode(command):
    invalidCommandCode = 127

    if command is None:
      return invalidCommandCode

    try:
      result = subprocess.run(command)
      return result.returncode

    except:
      return invalidCommandCode