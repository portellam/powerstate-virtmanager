#!/usr/local/bin/python

import sys
# import os
import subprocess
# from os import system

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
# print(text)

expression =  "echo {}" \
              .format(text)

# get_command_output(expression)
print(get_command_output(expression))
