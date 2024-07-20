#!/usr/local/bin/python

#
# Filename:       bash.py
# Version:        1.0.0
# Description:    Bash input and output logic for Python.
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

  def get_string_literal(string):
    return  "\"{}\"" \
            .format(string)

  # def get_variable(reference):
  #   return  "\"{}\"" \
  #           .format(string)

  text = get_command_input()

  expression =  "echo {}" \
                .format(text)

  print(get_command_output(expression))
