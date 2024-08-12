#!/usr/bin/env python3

#
# Filename:       domain.py
# Version:        1.0.0
# Description:    Virtual Machine object, logic, and actions.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

#
# TODO:
# - [ ] gracefully fail if you cannot parse info for one domain.
# - [x] add properties.
# - [x] add functions as defined in notes.
# - [ ] add unit tests.
# - [ ] add hypervisor validation (1. find strings, 2. implement).
# - [ ] add logic to check for virsh command.

import sys

from .command import Command

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

    self.command  = "{} {}".format( \
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
    Else, pass.
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
      info = Command(this_command).get_output_as_string()

    except:
      print("Exception: Cannot get information for '{}'".format(self.name))
      raise

    for line in info:
      if line.startswith("UUID:"):
        self.uuid = line.split(":")[1].split(" ")[1]
        continue

      if line.startswith("Name:"):
        self.name = line.split(":")[1].split(" ")[1]
        continue

      if line.startswith("Autostart:"):
        self.has_autostart = line.split(":")[1].split(" ")[1]
        continue

      if line.startswith("OS Type:"):
        self.hypervisor = line.split(":")[1].split(" ")[1]
        continue

      if line.startswith("Persistent:"):
        self.is_persistent = line.split(":")[1].split(" ")[1]
        continue

      if line.startswith("State:"):
        self.power_state = line.split(":")[1].split(" ")[1]
        continue

  # Begin: Auto-start logic.
  def disable_autostart(self):
    this_command =  "{} autostart --disable".format(self.command)

    try:
      code = Command.get_code(this_command)

      if code != 0:
        print("Failed to disable auto-start for '{}'.".format(self.name))
        sys.exit(1)

    except:
      print("Exception: Failed to disable auto-start for '{}'.".format(self.name))
      sys.exit(1)

    print("Disabled auto-start for '{}'.".format(self.name))

  def enable_autostart(self):
    this_command =  "{} autostart".format(self.command)

    try:
      code = Command.get_code(this_command)

    except:
      print("Exception: Failed to enable auto-start for '{}'.".format(self.name))
      sys.exit(1)

    if code != 0:
      print("Failed to enable auto-start for '{}'.".format(self.name))
      sys.exit(1)

    print("Enabled auto-start for '{}'.".format(self.name))

  # End: Auto-start logic.

  # Begin: Hypervisor validation.
  def is_hypervisor_qemu(self):
    return self.hypervisor.lower() == "hvf" \
      or self.hypervisor.lower() == "kvm" \
      or self.hypervisor.lower() == "qemu"

  def is_hypervisor_vmware_workstation(self):
    return self.hypervisor.lower().__contains__("vmware") \
      and ( \
        self.hypervisor.lower().__contains__("workstation") \
          or self.hypervisor.lower().__contains__("player")
      )
  # End: Hypervisor validation.

  # Begin: Power-state getters and setters.

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

  def set_power_state_argument(self):
    match self.power_state:
      case "paused":
        self.argument = "resume"

      case "pmsuspended":
        self.argument = "dompmwakeup"

      case "shut off":
        self.argument = "start"

      case _:
        sys.exit(1)

  def get_power_state_error( \
    self,
    new_power_state
  ):
    if not self.is_new_power_state_valid(new_power_state):
      return

    power_state_verb = self.power_state

    match self.power_state:
      case "pmsuspended":
        power_state_verb = "sleeping."

    print("Error: Cannot {} '{}'. Virtual machine is {}".format( \
      new_power_state,
      self.name,
      power_state_verb
    ))

  def get_power_state_verb( \
    self,
    power_state
  ):
    match power_state:
      case "dompmwakeup":
        return "wake"

      case "pmsuspended":
        return "sleep"

      case _:
        return power_state

  def is_new_power_state_valid( \
    self,
    new_power_state
  ):
    if new_power_state is not None \
      and new_power_state != "":
      print("Error: New power state {} is not valid.".format(new_power_state))

    match new_power_state:
      case "start" \
        | "resume" \
        | "wake":
        return self.power_state != "running"

      case "sleep" \
        | "hybrid sleep":
        return self.power_state != "pmsuspended"

      case "pause" \
        | "hibernate" \
        | "reboot" \
        | "reset" \
        | "stop" \
        | "force stop":
        return  self.power_state == "running"

      case _:
        print("Error: New power state is not valid.")
        return False

  def set_power_state( \
    self,
    argument
  ):
    if argument is None \
      or argument == "":
      sys.exit(1)

    this_command =  "{} {} {}".format( \
                      self.command,
                      argument,
                      self.command_suffix
                    )

    verb = self.get_power_state_verb(argument)

    try:
      code = Command.get_code(this_command)

    except Exception as contextManager:
      message = "Exception: Failed to {} '{}'.".format( \
        verb,
        self.name
      )

      print(contextManager.exception.output)
      print(message)
      raise

    if code != 0:
      message = "Error: Failed to {} '{}'.".format( \
        verb,
        self.name
      )

      print(message)
      sys.exit(1)

  # End: Power-state getters and setters.

  # Begin: Power-state action logic.
  def force_stop(self):
    if self.power_state != "running":
      self.get_power_state_error(self.power_state)
      sys.exit(1)

    self.set_power_state("destroy --domain")

  def hibernate(self):
    if self.power_state != "running":
      self.get_power_state_error(self.power_state)
      sys.exit(1)

    self.set_power_state("dompmsuspend --target disk")

  def hybrid_sleep(self):
    if self.power_state != "running":
      self.get_power_state_error(self.power_state)
      sys.exit(1)

    self.set_power_state("dompmsuspend --target hybrid")

  def pause(self):
    if self.power_state != "running":
      self.get_power_state_error(self.power_state)
      sys.exit(1)

    self.set_power_state("pause --domain")

  def reset(self):
    if self.power_state != "running":
      self.get_power_state_error(self.power_state)
      sys.exit(1)

    self.set_power_state("reset --domain")

  def restart(self):
    if self.power_state != "running":
      self.get_power_state_error(self.power_state)
      sys.exit(1)

    self.set_power_state("reboot --domain")

  def start(self):
    argument = ""

    match self.power_state:
      case "paused":
        argument = "resume --domain"

      case "pmsuspended":
        argument = "dompmwakeup --domain"

      case "shut off":
        argument = "start --domain"

      case _:
        self.get_power_state_error(self.power_state)
        sys.exit(1)

    self.set_power_state(argument)

  def sleep(self):
    if self.power_state != "running":
      self.get_power_state_error(self.power_state)
      sys.exit(1)

    self.set_power_state("dompmsuspend --target mem")

  def stop(self):
    if self.power_state != "running":
      self.get_power_state_error(self.power_state)
      sys.exit(1)

    self.set_power_state("shutdown --domain")
  # End: Power-state action logic.