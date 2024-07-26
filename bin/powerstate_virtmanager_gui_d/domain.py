#!/usr/bin/env python

#
# Filename:       domain.py
# Version:        1.0.0
# Description:    Virtual Machine logic.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

import sudo

class Domain:
  name  = ""
  state = ""
  command_prefix =  "virsh"
  command_suffix =  "--domain {}" \
                    .format(
                      name
                    )

  if sudo.is_sudo:
    command_prefix += "{} {}" \
                      .format(
                        sudo.command,
                        command_prefix
                      )

  def __init__(name, state):
    self.name   = name
    self.state  = state

  def is_valid():
    return name is not None

  def get_state():
    if is_valid():
      sys.exit(1)

    reference_name = ""

    command = "{} domstate {} | head --lines 1" \
                .format(
                  command_prefix,
                  command_suffix,
                )
    try:
      subprocess.run(command)

    except:
      message = "Exception: Failed to get power state for '{}'." \
                .format(name)

      print(message)
      __init__()
      sys.exit(1)