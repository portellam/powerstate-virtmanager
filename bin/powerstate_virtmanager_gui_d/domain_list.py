#!/usr/bin/env python

#
# Filename:       domain.py
# Version:        1.0.0
# Description:    List, select, and act on Virtual machines.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

#
# TODO:
# - [ ] gracefully fail if you cannot parse info for one domain.
# - [ ] add unit tests.
# - [ ] test how long it will take to parse all domains and their properties
# (example: running virsh many times).
# - [ ] determine upper memory limits of virsh, python stack, and glade GUI.
# - [ ] set upper limit?
# - [ ] add sort by.
# - [ ] add hypervisor validation.
# - [ ] add power state action logic.
#

from command  import Command
from domain   import Domain

class DomainList:
  list[Domain]    = []
  selected_list   = []
  command         = "virsh"
  argument        = "list"
  command_suffix  = "| head"

  def __init__(self):
    self.list = self.get_all()
    self.selected_list = []

  def get_command_with_option( \
    self,
    option
  ):
    return "{} {} {} {}".format( \
      self.command,
      self.argument,
      option,
      self.command_suffix
    )

  # Begin: Domain enum getters.
  def get_all(self):
    list[Domain] = []

    name_list = Command.get_output_as_list( \
      self.get_command_with_option("--all --name")
    )

    for name in name_list:
      try:
        list.add(Domain(name))

      except:
        continue

    return list

  # End: Domain enum getters.

  # Begin: Domain hypervisor sort logic.
  def get_qemu(self):
    list[Domain] = []

    for domain in self.list:
      if domain.is_hypervisor_qemu():
        continue

      try:
        list.add(domain)

      except:
        continue

    return list

  def get_vmware_workstation(self):
    list[Domain] = []

    for domain in self.list:
      if domain.is_hypervisor_vmware_workstation():
        continue

      try:
        list.add(domain)

      except:
        continue

    return list
  # End: Domain hypervisor sort logic.

  # Start: Domain power-state action logic.

  # End: Domain power-state action logic.