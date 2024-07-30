#!/usr/bin/env python

#
# Filename:       domain.py
# Version:        1.0.0
# Description:    Virtual Machine logic.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

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
  power_state       = ""
  command           = "virsh"
  argument          = ""
  command_suffix    = "| head --lines 1"

  def __init__( \
    self,
    name,
    state
  ):
    self.name     = name
    self.state    = state

    self.command  = "{} --domain {}".format( \
                      self.command,
                      self.name
                    )

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
      Command.get_output_as_string(this_command)

    except:
      message = "Exception: Failed to disable auto-start for '{}'." \
                  .format(self.name)

      print(message)
      sys.exit(1)


  def enable_autostart(self):
    this_command =  "{} autostart --disable".format(self.command)

    try:
      Command.get_output_as_string(this_command)

    except:
      message = "Exception: Failed to disable auto-start for '{}'." \
                  .format(self.name)

      print(message)
      sys.exit(1)