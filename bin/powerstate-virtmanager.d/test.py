#!/usr/local/bin/python

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
