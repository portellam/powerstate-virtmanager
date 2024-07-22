#!/usr/local/bin/python

#
# Filename:       BashDatatype.py
# Version:        1.0.0
# Description:    Bash datatype logic.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

import subprocess
import sys
from Bash.BashCommand import *

class BashDatatype:
  def GetFormattedArray(reference):
    if reference is None:
      sys.exit(1)

    return "\"${" + {reference} + "[*]}\""

  def GetFormattedArrayLength(reference):
    if reference is None:
      sys.exit(1)

    return "\"${#" + {reference} + "[*]}\""

  def GetFormattedKeys(reference):
    if reference is None:
      sys.exit(1)

    return "\"${!" + {reference} + "[*]}\""

  def GetFormattedVariable(reference):
    if reference is None:
      sys.exit(1)

    return "\"${" + {reference} + "}\""

  def GetKeysOutput(reference):
    command = "echo {}" \
              .format(GetFormattedKeys(reference))

    return GetOutput(command)

  def GetVariableOutput(reference):
    command = "echo {}" \
              .format(GetFormattedVariable(reference))

    return GetOutput(command)

  def GetStringLiteral(string):
    return  "\"{}\"" \
            .format(string)

  def IsArray(reference):
    if reference is None:
      sys.exit(1)

    command = "declare -p {} | grep \"-a\"" \
              .format(reference)

    try:
      result = BashCommand.GetCode(reference)

    except Exception exception:
      return False

    return result == 0

  def IsDictionary(reference):
    if reference is None:
      sys.exit(1)

    command = "declare -p {} | grep \"-A\"" \
              .format(reference)

    try:
      result = BashCommand.GetCode(reference)

    except Exception exception:
      return False

    return result == 0

  def IsVariable(reference):
    if reference is None:
      sys.exit(1)

    command = "declare -p {}" \
              .format(reference)

    try:
      result = BashCommand.GetCode(reference)

    except Exception exception:
      return False

    return result == 0