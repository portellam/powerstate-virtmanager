#!/bin/bash

local -r str_script_file="powerstate-virtmanager-script-dialog.sh"
local -r str_source_file="script-dialog"

if [[ -e "${str_script_file}" ]]; then
  echo "Error: Cannot locate script file."
  return 1
fi

if [[ -e "${str_source_file} ]]; then
  echo "Error: Cannot locate source file."
  return 1
fi

local 

if ! cp 
