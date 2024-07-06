#!/bin/bash/env bash

#
# Filename:       pwrstatevirtman.bash
# Description:    Bash commandline tool for Power State Virtual Machine Manager.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

#
# parameters
#
  declare -r str_command="virsh"

#
# logic
#
    function select_option
    {
      echo -e "" \
        "Do what now?\n" \
        "1. Start\n" \
        "2. Pause\t(freeze CPU time)\n" \
        "3. Shutdown\t(Power off)\n" \
        "4. Resume from Hibernation\n" \
        "5. Start domain\n" \
        "6. Start domain\n" \

      case "${1}" in
        ""

      esac
    }

  #
  # DESC: Main
  #
    function main
    {
      return 0
    }

  #
  # DESC: Datatype logic
  #
    function is_string
    {
      if [[ "${1}" == "" ]]; then
        return 1
      fi

      return 0
    }

  #
  # DESC: Domain State Logic
  #
    function force_stop_domain
    {
      if is_domain_online "${1}"; then
        return 255
      fi

      if ! ${str_command} destroy "${1}"; then
        return 1
      fi

      return 0
    }

    function hard_stop_domain
    {
      if is_domain_online "${1}"; then
        return 255
      fi

      if ! ${str_command} shutdown "${1}"; then
        return 1
      fi

      return 0
    }

    function power_start_domain
    {
      if is_domain_online "${1}"; then
        return 255
      fi

      if ! ${str_command} dompmwakeup "${1}"; then
        return 1
      fi

      return 0
    }

    function power_stop_domain
    {
      if is_domain_online "${1}"; then
        return 255
      fi

      if ! ${str_command} dompmsuspend "${1}"; then
        return 1
      fi

      return 0
    }

    function soft_start_domain
    {
      if is_domain_online "${1}"; then
        return 255
      fi

      if ! ${str_command} resume "${1}"; then
        return 1
      fi

      return 0
    }

    function soft_stop_domain
    {
      if is_domain_online "${1}"; then
        return 255
      fi

      if ! ${str_command} suspend "${1}"; then
        return 1
      fi

      return 0
    }

  #
  # DESC: Domain Validation
  #
    function does_domain_exist
    {
      if ! is_string "${1}"; then
        return 255
      fi

      if ! ${str_command} list --all | grep "${1}"; then
        return 1
      fi

      return 0
    }

    function is_domain_online
    {
      if ! does_domain_exist "${1}"; then
        return 255
      fi

      if ! ${str_command} list --state-running | grep "${1}"; then
        return 1
      fi

      return 0
    }

  #
  # DESC: Presentation Logic
  #

