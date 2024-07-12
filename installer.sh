#!/bin/bash

#
# Filename:       installer.sh
# Version:        1.0.0
# Description:    Install executable and source files.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

function is_user_root
  {
    if [[ $( whoami ) != "root" ]]; then
      echo "User is not root."
      return 1
    fi

    return 0
  }

function install
{
  local -r relative_path="bin"
  local -r script_file="powerstate-virtmanager"

  if [[ ! -e "${relative_path}/${script_file}" ]]; then
    echo "Error: Cannot locate script file."
    return 1
  fi

  local -r source_file="powerstate-virtmanager.d/script-dialog"

  if [[ ! -e "${relative_path}/${source_file}" ]]; then
    echo "Error: Cannot locate source file."
    return 1
  fi

  local -r destination_path="/usr/local/bin"

  if ! cp --force --recursive "${relative_path}/${script_file}" \
    "${destination_path}/${script_file}" &> /dev/null; then
    echo "Error: Cannot copy script file."
    return 1
  fi

  if ! mkdir --parents $( dirname "${destination_path}/${source_file}" ) \
    &> /dev/null; then
    echo "Error: Cannot copy script file."
    return 1
  fi

  if ! cp --force --recursive "${relative_path}/${source_file}" \
    "${destination_path}/${source_file}" &> /dev/null; then
    echo "Error: Cannot copy source file."
    return 1
  fi

  if ! chmod +x "${destination_path}/${script_file}" \
    &> /dev/null; then
    echo "Error: Cannot set script file as executable."
    return 1
  fi

  if ! chmod +x "${destination_path}/${source_file}" \
    &> /dev/null; then
    echo "Error: Cannot set source file as executable."
    return 1
  fi

  return 0
}

function main
{
  if ! is_user_root \
    || ! install; then
    echo "Install failed."
    return 1
  fi

  echo "Install successful."
  return 0
}

main
exit "${?}"