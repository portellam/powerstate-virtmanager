#!/usr/local/bin/python

#
# Filename:       bash_output.py
# Version:        1.0.0
# Description:    Bash to Python logic.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

import subprocess
import sys

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

def get_string_literal(string):
  return  "\"{}\"" \
          .format(string)

text = sys.stdin.readline()

expression =  "echo {}" \
              .format(text)

print(get_command_output(expression))
