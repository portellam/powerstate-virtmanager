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
  # @property
  invalid_command_code = 127

  def GetCommandInput():
    try:
      result = sys.stdin.readline()
      return result

    except Exception as contextManager:
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

    except subprocess.CalledProcessError as contextManager:
      print(exception)
      sys.exit(1)

  def GetCommandReturnCode(command):
    if command is None:
      print("Command does not exist.")
      return 127

    try:
      result = subprocess.run(command)
      return result.returncode

    except:
      print("Command does not exist.")
      return 127

  # Test function
  def Example(input):
    if input is None:
      sys.exit(1)

    return 0