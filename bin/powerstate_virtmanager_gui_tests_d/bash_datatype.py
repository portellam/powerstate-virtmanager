#!/usr/local/bin/python

#
# Filename:       bash_datatype.py
# Version:        1.0.0
# Description:    Bash datatype logic.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

import re
import sys
from bash_command import BashCommand

class BashDatatype(object):
  def GetFormattedArray(
    self,
    reference
  ):
    if not self.IsReferenceLegal(reference):
      sys.exit(1)

    return "\"${" + reference + "[*]}\""

  def GetFormattedArrayLength(
    self,
    reference
  ):
    if not self.IsReferenceLegal(reference):
      sys.exit(1)

    return "\"${#" + reference + "[*]}\""

  def GetFormattedKeys(
    self,
    reference
  ):
    if not self.IsReferenceLegal(reference):
      sys.exit(1)

    return "\"${!" + reference + "[*]}\""

  def GetFormattedVariable(
    self,
    reference
  ):
    if not self.IsReferenceLegal(reference):
      sys.exit(1)

    return "\"${" + reference + "}\""

  def GetKeysOutput(
    self,
    reference
  ):
    if not self.IsReferenceLegal(reference):
      sys.exit(1)

    command = "echo {}" \
              .format(GetFormattedKeys(reference))

    return GetOutput(command)

  def GetVariableOutput(
    self,
    reference
  ):
    if not self.IsReferenceLegal(reference):
      sys.exit(1)

    command = "echo {}" \
              .format(GetFormattedVariable(reference))

    return GetOutput(command)

  def GetStringLiteral(
    self,
    string
  ):
    if string is None:
      string = ""

    return  "\"{}\"" \
            .format(string)

  def IsArray(
    self,
    reference
  ):
    if not self.IsReferenceLegal(reference):
      sys.exit(1)

    command = "declare -p {} | grep \"-a\"" \
              .format(reference)

    try:
      result = BashCommand.RunCommand(reference).code

    except Exception as contextManager:
      return False

    return result == 0

  def IsDictionary(
    self,
    reference
  ):
    if not self.IsReferenceLegal(reference):
      sys.exit(1)

    command = "declare -p {} | grep \"-A\"" \
              .format(reference)

    try:
      result = BashCommand.RunCommand(reference).code

    except Exception as contextManager:
      return False

    return result == 0

  def IsReferenceLegal(
    self,
    reference
  ):
    if reference is None \
      or reference == "":
      return False

    pattern = re.compile("^[a-zA-Z0-9_]*$")
    return bool(pattern.search(reference))

  def IsVariable(
    self,
    reference
  ):
    if not self.IsReferenceLegal(reference):
      sys.exit(1)

    command = "declare -p {}" \
              .format(reference)

    try:
      result = BashCommand.RunCommand(reference).code

    except Exception as contextManager:
      return False

    return result == 0
