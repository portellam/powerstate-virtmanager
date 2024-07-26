#!/usr/bin/env python

#
# Filename:       bash_enum.py
# Version:        1.0.0
# Description:    Enum datatype logic between Bash and Python.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

from os import system

class bash_enum:
  enum = []

  def __init__(enum):
    self.enum = enum

  def set_enum_from_reference(reference_name):
    __init__(reference_name)

  def get_enum_from_reference(reference_name):
    if reference_name is None:
      sys.exit(1)

    reference_expression = '"${' + reference_name + '[@]}"'

    enum =  "$( python -c 'import sys; " \
            "from pyscript import {}; print {}(sys.argv[1:])' {} )" \
            .format(
              BashClass.set_enum_from_reference.__name__,
              BashClass.set_enum_from_reference.__name__,
              reference_expression
            )

    set_enum =  "mapfile -t {} <<<\"${}\"" \
                .format(
                  reference_name,
                  enum.__name__
                )

    try:
      subprocess.run(enum)

    except:
      exception_message = "Exception: Failed to get enumeration."
      print(exception_message)
      __init__()
      sys.exit(1)

    try:
      subprocess.run(set_enum)

    except:
      exception_message = "Exception: Failed to set enumeration."
      print(exception_message)
      __init__()
      sys.exit(1)