#!/bin/bash

#
# Filename:       powerstate-virtmanager.sh
# Version:        1.0.0-alpha
# Description:    Set the power state of a QEMU/KVM Virtual Machine (VM).
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

#
# sources
#
  SCRIPT_DIR="$( \
      cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd \
    )/powerstate-virtmanager.d"

  # shellcheck source=./script-dialog
  source "${SCRIPT_DIR}"/script-dialog

#
# params
#
  SCRIPT_FILE="pwrstate-virtman-script-dialog.sh"
  LOG_FILE="/var/log/${SCRIPT_FILE}.log"
  APP_NAME="Power State VM Manager"

  #GUI=false; terminal=false  # force relaunching as if launching from GUI without
                              # a GUI interface installed, but only do this for
                              # testing

  #NOSYMBOLS=true
  #NOCOLORS=true

  readonly MAX_LIST_SIZE=5  # boxes currently have issues with lists greater
                            # than 5.

#
# logic
#
  function main
  {
    local domain=""

    if ! is_user_root \
      || ! prompt_virtual_machines "domain" \
      || ! prompt_power_states "${domain}"; then
      return 1
    fi

    return 0
  }

  function is_user_root
  {
    if [[ $( whoami ) != "root" ]]; then
      message-error "User is not root."
      return 1
    fi

    return 0
  }

  function prompt_power_states
  {
    local selected_domain="${1}"

    if [[ "${selected_domain}" == "" ]]; then
      message-error "Invalid virtual machine selected."
      return 1
    fi

    local domain_state="$( \
      sudo virsh domstate "${selected_domain}" | head --lines 1 \
    )"

    ACTIVITY="POWER STATES"

    ANSWER=$( \
      radiolist "Set Power State for ${selected_domain}" 5  \
        "Start"         "Resume any suspended state."           OFF \
        "Pause"         "Suspend state."                        OFF \
        "Sleep"         "Suspend to Memory (S3)"                OFF \
        "Hibernate"     "Suspend to Disk (S4)"                  OFF \
        "Hybrid Sleep"  "Suspend to Memory (S3) and Disk (S4)"  OFF \
        "Stop"          "Suspend power (S5)."                   OFF \
        "Force Stop"    "Force suspend power (S5)."             OFF
    )

    local -Ar power_states_and_choice=(
      ["start"]="start"
      ["resume"]=resume
      ["wake"]="dompmwakeup"
      ["pause"]="suspend"
      ["sleep"]="dompmsuspend --target mem"
      ["hibernate"]="dompmsuspend --target disk"
      ["hybrid sleep"]="dompmsuspend --target hybrid"
      ["stop"]="shutdown"
      ["force stop"]="destroy"
    )

    local -Ar power_states_and_status=(
      ["start"]="running"
      ["pause"]="paused"
      ["sleep"]="pmsuspended"
      ["hibernate"]="shut off"
      ["hybrid sleep"]="pmsuspended"
      ["stop"]="shut off"
      ["force stop"]="shut off"
    )

    ANSWER="${ANSWER,,}"  # to lowercase.
    local option=""

    case "${ANSWER}" in
      "pause" \
        | "sleep" \
        | "hibernate" \
        | "hybrid sleep" \
        | "stop" \
        | "force stop" \
      )
        if [[ "${domain_state}" != "${power_states_and_status["start"]}" ]]; then
          message-warn "Cannot stop Virtual Machine. VM is offline."
          return 1
        fi
        ;;

      "start" )
        if [[ "${domain_state}" == "${power_states_and_status["start"]}" ]]; then
          message-warn "Cannot start Virtual Machine. VM is online."
          return 255
        fi

        case "${domain_state}" in
          "${power_states_and_status["pause"]}" )
            ANSWER="resume"
            ;;

          "${power_states_and_status["stop"]}" )
            ANSWER="start"
            ;;

          "${power_states_and_status["sleep"]}" )
            ANSWER="wake"
            ;;
        esac
        ;;

      "" )
        message-error "No power state selected."
        return 1
        ;;
    esac

    option="${power_states_and_choice["${ANSWER}"]}"

    if [[ "${option}" == "" ]]; then
      message-error "Unsupported power state '${ANSWER}'."
      return 1
    fi

    local set_domain_power_state="sudo virsh ${option} --domain ${selected_domain}"

    if ! eval "${set_domain_power_state}"; then
      message-error "Failed to ${ANSWER} Virtual Machine."
      return 1
    fi

    return 0
  }

    function prompt_virtual_machines
  {
    local -n reference="${1}"
    ACTIVITY="VIRTUAL MACHINES"

    local -ir max_index="$( sudo virsh list --all --name | head | wc --lines )"

    if [[ "${max_index}" -eq 0 ]]; then
      message-warn "No virtual machines exist."
      return 1
    fi

    #dialog_to_evaluate="radiolist \"Select a Virtual Machine\" \"${max_index}\""
    dialog_to_evaluate="radiolist \"Select a Virtual Machine\" \"${MAX_LIST_SIZE}\""
    local -i index=1

    for domain in $( sudo virsh list --all --name | head ); do
      dialog_to_evaluate+=" \\ \"${index}.\" \"${domain}\" OFF"
      (( index++ ))
    done

    ANSWER=$( eval "${dialog_to_evaluate}" )
    local selected_index="$( echo "${ANSWER}" | cut --delimiter '.' --fields 1 )"

    if [[ "${selected_index}" == "" ]]; then
      message-error "No virtual machine selected."
      return 1
    fi

    local selected_domain="$( \
      sudo virsh list --all --name | sed -n "${selected_index}p" \
    )"

    if [[ ${selected_domain} == "" ]]; then
      message-error "Invalid virtual machine selected."
      return 1
    fi

    reference="${selected_domain}"
    return 0
  }

#
# main
#
  relaunch-if-not-visible
  main