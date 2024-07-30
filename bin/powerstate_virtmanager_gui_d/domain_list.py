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
  list[Domain]          = []
  selected_list[Domain] = []
  selected_uuid_list    = []
  command               = "virsh"
  argument              = "list"
  command_suffix        = "| head"

  def __init__(self):
    self.list               = self.get_all()
    self.selected_list      = []
    self.selected_uuid_list = []

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

  # Begin: Domain selection.
  def deselect( \
    self,
    uuid
  ):
    domain = self.get_domain(uuid)

    if domain is None:
      print("Error: Invalid virtual machine.")
      return

    self.selected_list.remove(domain)
    print("Unselected virtual machine '{}'.".format(domain.name))

  def get_domain( \
    self,
    uuid
  ):
    if uuid is None \
      or uuid == "":
      return None

    for domain in list:
      if domain.uuid == uuid:
        return domain

    return None

  def has_selected(self):
    return not self.selected_list is None \
      and not self.selected_list.len == 0

  def select( \
    self,
    uuid
  ):
    domain = self.get_domain(uuid)

    if domain is None:
      print("Error: Invalid virtual machine selected.")
      return

    self.selected_list.add(domain)
    print("Selected virtual machine '{}'.".format(domain.name))

  # End: Domain selection.

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
  def force_stop_selected(self):
    if not self.has_selected():
      return

    has_failed = False

    for selected in self.selected_list:
      try:
        selected.force_stop()

      except:
        has_failed = True
        continue

    if has_failed:
      print("Error: Failed to force stop one or more virtual machines.")

  def hibernate_selected(self):
    if not self.has_selected():
      return

    has_failed = False

    for selected in self.selected_list:
      try:
        selected.hibernate()

      except:
        has_failed = True
        continue

    if has_failed:
      print("Error: Failed to hibernate one or more virtual machines.")

  def hybrid_sleep_selected(self):
    if not self.has_selected():
      return

    has_failed = False

    for selected in self.selected_list:
      try:
        selected.hybrid_sleep()

      except:
        has_failed = True
        continue

    if has_failed:
      print("Error: Failed to hybrid sleep one or more virtual machines.")

  def pause_selected(self):
    if not self.has_selected():
      return

    has_failed = False

    for selected in self.selected_list:
      try:
        selected.pause()

      except:
        has_failed = True
        continue

    if has_failed:
      print("Error: Failed to pause one or more virtual machines.")

  def pause_selected(self):
    if not self.has_selected():
      return

    has_failed = False

    for selected in self.selected_list:
      try:
        selected.pause()

      except:
        has_failed = True
        continue

    if has_failed:
      print("Error: Failed to pause one or more virtual machines.")

  def restart_selected(self):
    if not self.has_selected():
      return

    has_failed = False

    for selected in self.selected_list:
      try:
        selected.restart()

      except:
        has_failed = True
        continue

    if has_failed:
      print("Error: Failed to restart one or more virtual machines.")

  def reset_selected(self):
    if not self.has_selected():
      return

    has_failed = False

    for selected in self.selected_list:
      try:
        selected.reset()

      except:
        has_failed = True
        continue

    if has_failed:
      print("Error: Failed to reset one or more virtual machines.")

  def restart_selected(self):
    if not self.has_selected():
      return

    has_failed = False

    for selected in self.selected_list:
      try:
        selected.restart()

      except:
        has_failed = True
        continue

    if has_failed:
      print("Error: Failed to restart one or more virtual machines.")

  def start_selected(self):
    if not self.has_selected():
      return

    has_failed = False

    for selected in self.selected_list:
      try:
        selected.start()

      except:
        has_failed = True
        continue

    if has_failed:
      print("Error: Failed to start one or more virtual machines.")

  def sleep_selected(self):
    if not self.has_selected():
      return

    has_failed = False

    for selected in self.selected_list:
      try:
        selected.sleep()

      except:
        has_failed = True
        continue

    if has_failed:
      print("Error: Failed to sleep one or more virtual machines.")

  def stop_selected(self):
    if not self.has_selected():
      return

    has_failed = False

    for selected in self.selected_list:
      try:
        selected.stop()

      except:
        has_failed = True
        continue

    if has_failed:
      print("Error: Failed to stop one or more virtual machines.")

  # End: Domain power-state action logic.