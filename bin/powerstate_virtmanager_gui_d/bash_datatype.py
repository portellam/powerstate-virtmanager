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
from bash_command import BashCommand

class BashDatatype:
  def GetFormattedArray(reference):
    if reference is None \
      or reference == "":
      sys.exit(1)

    return "\"${" + reference + "[*]}\""

  def GetFormattedArrayLength(reference):
    if reference is None \
      or reference == "":
      sys.exit(1)

    return "\"${#" + reference + "[*]}\""

  def GetFormattedKeys(reference):
    if reference is None \
      or reference == "":
      sys.exit(1)

    return "\"${!" + reference + "[*]}\""

  def GetFormattedVariable(reference):
    if reference is None \
      or reference == "":
      sys.exit(1)

    return "\"${" + reference + "}\""

  def GetKeysOutput(reference):
    command = "echo {}" \
              .format(GetFormattedKeys(reference))

    return GetOutput(command)

  def GetVariableOutput(reference):
    command = "echo {}" \
              .format(GetFormattedVariable(reference))

    return GetOutput(command)

  def GetStringLiteral(string):
    if string is None:
      string = ""

    return  "\"{}\"" \
            .format(string)

  def IsArray(reference):
    if reference is None \
      or reference == "":
      sys.exit(1)

    command = "declare -p {} | grep \"-a\"" \
              .format(reference)

    try:
      result = BashCommand.GetCode(reference)

    except Exception as contextManager:
      return False

    return result == 0

  def IsDictionary(reference):
    if reference is None \
      or reference == "":
      sys.exit(1)

    command = "declare -p {} | grep \"-A\"" \
              .format(reference)

    try:
      result = BashCommand.GetCode(reference)

    except Exception as contextManager:
      return False

    return result == 0

  def IsVariable(reference):
    if reference is None \
      or reference == "":
      sys.exit(1)

    command = "declare -p {}" \
              .format(reference)

    try:
      result = BashCommand.GetCode(reference)

    except Exception as contextManager:
      return False

    return result == 0