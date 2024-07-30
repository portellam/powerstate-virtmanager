#!/usr/bin/env python

#
# Filename:       domain.py
# Version:        1.0.0
# Description:    Virtual Machine logic.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

# TODO: gracefully fail if you cannot parse info for one domain.

import sys

from command import Command

class Domain:
  uuid              = ""
  name              = ""
  has_autostart     = False
  has_checkpoint    = False
  has_managed_save  = False
  has_snapshot      = False
  hypervisor        = ""
  is_persistent     = False
  power_state       = ""
  command           = "virsh"
  argument          = ""
  command_suffix    = "| head --lines 1"

  """_summary_
    Constructor
  """
  def __init__( \
    self,
    name
  ):
    self.name = name

    self.command  = "{} --domain {}".format( \
                      self.command,
                      self.name
                    )

    try:
      self.set_info()

    except:
      sys.exit(1)

  """_summary_
    Parses the domain information by command line.
    Sets the constructor properties given valid information.
    If the name is Null or an empty string, exit with failure.
    If parse is not successful, print exception and exit with failure.
  """
  def set_info(self):
    if self.name is None \
      or self.name == "":
      sys.exit(1)

    this_command =  "{} dominfo {}".format( \
                      self.command,
                      self.command_suffix,
                    )

    try:
      info = Command.get_output_as_list(this_command)

    except Exception as contextManager:
      print(contextManager.exception.output)
      print("Exception: Cannot get information for '{}'".format(self.name))
      raise

    self.uuid = info.startswith("UUID:").split(":")[1].split(" ")[1]
    self.name = info.startswith("Name:").split(":")[1].split(" ")[1]
    self.has_autostart = info.startswith("Autostart:").split(":")[1].split(" ")[1]
    self.hypervisor = info.startswith("OS Type:").split(":")[1].split(" ")[1]
    self.is_persistent = info.startswith("Persistent").split(":")[1].split(" ")[1]
    self.power_state = info.startswith("State:").split(":")[1].split(" ")[1]

  def get_power_state(self):
    this_command =  "{} domstate {}".format( \
                      self.command,
                      self.command_suffix,
                    )

    try:
      return Command.get_output_as_string(this_command)

    except:
      message = "Exception: Failed to get power state for '{}'.".format(self.name)
      print(message)
      sys.exit(1)

  def disable_autostart(self):
    this_command =  "{} autostart --disable".format(self.command)

    try:
      code = Command.get_code(this_command)

    except:
      message = "Exception: Failed to disable auto-start for '{}'." \
                  .format(self.name)

      print(message)
      sys.exit(1)

    if code != 0:
      print("Failed to disable auto-start for '{}'.".format(self.name))
      sys.exit(1)

    print("Disabled auto-start for '{}'.".format(self.name))

  def enable_autostart(self):
    this_command =  "{} autostart".format(self.command)

    try:
      code = Command.get_code(this_command)

    except:
      message = "Exception: Failed to enable auto-start for '{}'." \
                  .format(self.name)

      print(message)
      sys.exit(1)

    if code != 0:
      print("Failed to enable auto-start for '{}'.".format(self.name))
      sys.exit(1)

    print("Enabled auto-start for '{}'.".format(self.name))