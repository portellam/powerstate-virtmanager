#!/usr/bin/env python

#
# Filename:       bash_py_var.py
# Version:        1.0.0
# Description:    Variable datatype logic between Bash and Python.
# Author(s):      Alex Portell <github.com/portellam>
# Maintainer(s):  Alex Portell <github.com/portellam>
#

from os import system

class bash_var:
  var = []

  def __init__(var):
    self.var = var

  def set_var_from_reference(reference_name):
    __init__(reference_name)

  def get_var_from_reference(reference_name):
    if reference_name is None:
      sys.exit(1)

    reference_expression = '"${' + reference_name + '}"'

    var =  "$( python -c 'import sys; " \
            "from pyscript import {}; print {}(sys.argv[1:])' {} )" \
            .format(
              BashClass.set_var_from_reference.__name__,
              BashClass.set_var_from_reference.__name__,
              reference_expression
            )

    set_var =  "echo \"${}\" <<<\"${}\"" \
                .format(
                  reference_name,
                  var.__name__
                )

    try:
      subprocess.run(var)

    except:
      exception_message = "Exception: Failed to get variable."
      print(exception_message)
      __init__()
      sys.exit(1)

    try:
      subprocess.run(set_var)

    except:
      exception_message = "Exception: Failed to set variable."
      print(exception_message)
      __init__()
      sys.exit(1)