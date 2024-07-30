#!/usr/bin/env python

#
# Filename:       domain.py
# Version:        1.0.0
# Description:    Virtual Machine logic.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

#
# TODO:
# - [ ] gracefully fail if you cannot parse info for one domain.
# - [ ] add unit tests.
# - [ ] test how long it will take to parse all domains and their properties
# (example: running virsh many times).
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