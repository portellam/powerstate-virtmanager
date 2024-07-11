#!/bin/bash

#
# Filename:       installer.sh
# Version:        1.0.0
# Description:    Install executable and source files.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

function install
{
  local -r script_file="powerstate-virtmanager.sh"

  if [[ -e "./${script_file}" ]]; then
    echo "Error: Cannot locate script file."
    return 1
  fi

  local -r source_file="powerstate-virtmanager.d/script-dialog"

  if [[ -e "./${source_file}" ]]; then
    echo "Error: Cannot locate source file."
    return 1
  fi

  local -r destination_path="/usr/bin/local"

  if ! cp "./${script_file}" "${destination_path}/${script_file}" \
    &> /dev/null; then
    echo "Error: Cannot copy script file."
    return 1
  fi

  if ! cp "./${source_file}" "${destination_path}/${source_file}" \
    &> /dev/null; then
    echo "Error: Cannot copy source file."
    return 1
  fi

  if ! chmod +x "./${script_file}" "${destination_path}/${script_file}" \
    &> /dev/null; then
    echo "Error: Cannot set script file as executable."
    return 1
  fi

  if ! chmod +x "./${source_file}" "${destination_path}/${source_file}" \
    &> /dev/null; then
    echo "Error: Cannot set source file as executable."
    return 1
  fi

  return 0
}

function main
{
  if ! install; then
    echo "Install failed."
    return 1
  fi

  echo "Install successful."
  return 0
}

main
exit "${?}"