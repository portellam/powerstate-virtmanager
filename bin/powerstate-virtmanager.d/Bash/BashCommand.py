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

  def __init__(self):
    self.code = 1
    self.command = None
    self.output = None

  def __init__(self, command):
    self.code = 1
    self.command = command
    self.output = ""

  # TODO: how to determine command and code from input ?
  def SetInput():
    try:
      code = 127
      output = sys.stdin.readline()
      command = ""

    except:
      output = None
      command = None

  def SetOutput():
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
      __init__()

  def GetInput():
    try:
      return sys.stdin.readline()

    except Exception as contextManager:
      print(contextManager.exception)
      return None

  def GetOutput(command):
    if command is None:
      return None

    try:
      result = subprocess.run(
        command,
        capture_output = True,  # Python >= 3.7 only
        text = True             # Python >= 3.7 only
      )

      return result.stdout

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