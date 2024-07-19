#!/usr/bin/env python

#
# Filename:       bash_enum.py
# Version:        1.0.0
# Description:    Enum datatype logic between Bash and Python.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

class bash_enum:
  py_enum = []

    def __init__(py_enum):
      self.py_enum = py_enum

    def set_py_enum_from_bash_ref(bash_ref_name):
      __init__(bash_ref_name)

    def get_py_enum_from_bash_ref(bash_ref_name):
      if bash_ref_name is None:
        sys.exit(1)

      bash_ref_expression = '"${' + bash_ref_name + '[@]}"'

      py_enum =  "$( python -c 'import sys; " \
              "from pyscript import {}; print {}(sys.argv[1:])' {} )" \
              .format(
                BashClass.set_py_enum_from_bash_ref.__name__,
                BashClass.set_py_enum_from_bash_ref.__name__,
                bash_ref_expression
              )

      set_py_enum =  "mapfile -t {} <<<\"${}\"" \
                  .format(
                    bash_ref_name,
                    py_enum.__name__
                  )

      try:
        subprocess.run(py_enum)
      except:
        exception_message = "Exception: Failed to get enumeration."
        print(exception_message)
        __init__()
        sys.exit(1)

      try:
        subprocess.run(set_py_enum)
      except:
        exception_message = "Exception: Failed to set enumeration."
        print(exception_message)
        __init__()
        sys.exit(1)