#!/usr/local/bin/python

#
# Filename:       bash_datatype.py
# Version:        1.0.0
# Description:    Bash datatype logic.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

import subprocess
import sys
import bash_command

class bash:
  def get_formatted_array(reference):
    if reference is None:
      sys.exit(1)

    return "\"${" + reference "[*]}\""

  def get_formatted_array_length(reference):
    if reference is None:
      sys.exit(1)

    return "\"${#" + reference "[*]}\""

  def get_formatted_keys(reference):
    if reference is None:
      sys.exit(1)

    return "\"${!" + reference "[*]}\""

  def get_formatted_variable(reference):
    if reference is None:
      sys.exit(1)

    return "\"${" + reference "}\""

  def get_keys_output(reference):
    command = "echo {}" \
              .format(get_formatted_variable(reference))

    return get_command_output(command)

  def get_variable_output(reference):
    command = "echo {}" \
              .format(get_formatted_variable(reference))

    return get_command_output(command)

  def get_string_literal(string):
    return  "\"{}\"" \
            .format(string)



  def is_variable(reference):


  text = get_command_input()

  expression =  "echo {}" \
                .format(text)

  print(get_command_output(expression))
