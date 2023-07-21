from os import system

class BashEnum:
  enum = []

  def __init__(enum):
    self.enum = enum

  def set_enum_from_reference(ref):
    __init__(ref)

  def get_enum_from_reference(ref):
    if ref is None:
      sys.exit(1)

    expression = '"${' + ref + '[@]}"'
    enum = "$( python -c 'import sys; from pyscript import {}; print {}(sys.argv[1:])' {} )".format(BashClass.set_enum_from_reference.__name__, BashClass.set_enum_from_reference.__name__, expression)
    set_enum = "mapfile -t {} <<<\"${}\"".format(ref, enum.__name__)

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

class BashVar:
  var = ""

  def __init__(var):
    self.var = var

  def set_var_from_reference(ref):
    __init__(ref)

  def get_var_from_reference(ref):
    if ref is None:
      sys.exit(1)

    expression = '"${' + ref + '}"'
    var = "$( python -c 'import sys; from pyscript import {}; print {}(sys.argv[1:])' {} )".format(BashClass.set_var_from_reference.__name__, BashClass.set_var_from_reference.__name__, expression)
    set_var = "echo -e \"${}\"".format(ref, enum.__name__)

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

class Domain:
  command_prefix = "sudo virsh"

  option_list_all     = "list --all"
  option_hard_start   = "start"
  option_hard_stop    = "shutdown"
  option_soft_start   = "resume"
  option_soft_stop    = "suspend"
  option_power_start  = "dompmwakeup"
  option_power_stop   = "dompmsuspend"

  option_set_domain     = "--domain"
  option_set_target     = "--target"
  option_target_both    = "hybrid"
  option_target_disk    = "disk"
  option_target_memory  = "mem"

  state_paused    = "paused"
  state_started   = "running"
  state_stopped   = "shut off"
  state_stop      = "pmsuspended"

  set_hard_start_domain   = "{} {} ".format(command_prefix,option_hard_start)
  set_hard_stop_domain    = "{} {} ".format(command_prefix,option_hard_stop)

  set_power_start_domain                    = "{} {} ".format(command_prefix,option_power_start)
  set_power_stop_domain_to_disk             = "{} {} {} {} ".format(command_prefix,option_set_target,option_target_disk,option_set_domain)
  set_power_stop_domain_to_disk_and_memory  = "{} {} {} {} ".format(command_prefix,option_set_target,option_target_both,option_set_domain)
  set_power_stop_domain_to_memory           = "{} {} {} {} ".format(command_prefix,option_set_target,option_target_memory,option_set_domain)

  set_soft_start_domain = "{} {} ".format(command_prefix,option_soft_start)
  set_soft_stop_domain  = "{} {} ".format(command_prefix,option_soft_stop)

  def __init__(self, domain, domain_list, status_list):
    self.domain = domain
    self.domain_list = domain_list
    self.status_list = status_list

  def do_hard_start_domain():
    __run_command_with_domain(set_hard_start_domain)

  def do_hard_stop_domain():
    __run_command_with_domain(set_hard_stop_domain)

  def do_power_stop_domain_to_disk():
    __run_command_with_domain(set_power_stop_domain_to_disk)

  def do_power_stop_domain_to_disk_and_memory():
    __run_command_with_domain(set_power_stop_domain_to_disk_and_memory,)

  def do_power_stop_domain_to_memory():
    __run_command_with_domain(set_power_stop_domain_to_memory)

  def do_soft_start_domain():
    __run_command_with_domain(set_soft_start_domain)

  def do_soft_stop_domain():
    __run_command_with_domain(set_soft_stop_domain)

  def get_domain_status():
    if self.domain not in self.domain_list:
      syscall.exit(1)

    i = self.domain_list.index(self.domain)
    self.status = self.domain_list(i)

  def get_lists():
    __get_domain_list()
    __get_status_list()

  def __get_domain_list():
    list_ref = "_ARR_DOMAIN"
    get_domain_list = "{} {} {}".format(command_prefix, option_list_all, option_set_domain)
    set_ref = "declare -a {}=$( {} )".format(list_ref, get_domain_list)
    subprocess.run(set_ref)
    BashClass.get_enum_from_reference(list_ref)
    self.domain_list = BashClass.enum

    if self.domain_list is None:
      sys.exit(1)

  def __get_status_list():
    domain_ref = "_DOMAIN"
    element_ref = "_ELEMENT"
    get_domain_list = "{} {} {}".format(command_prefix, option_list_all, option_set_domain)
    get_messy_domain_and_state = "{} {} | grep '${}' | head -n 1 '".format(command_prefix, option_list_all, domain_ref)

    for domain in self.domain_list:
      set_domain = "declare -a {}=\"{}\"".format(domain_ref, domain)
      line = ""

      while True:
        index=2
        get_delimited_value = "| awk 'END {print $" + index + "}'"
        get_element = "declare {}=$( \"{}{}\" )".format(element_ref, get_messy_domain_and_state, get_delimited_value)
        subprocess.run(get_element)
        BashVar.set_var_from_reference(element_ref)

        if BashVar.var is None:
          break

        line.__add__("{} ".format(BashVar.var))
        index.__add__(1)

      self.status_list.append(line)

    if self.status_list is None:
      sys.exit(1)

  def __get_filtered_domain_state():
    if line is None:
      return ""

    wordList = line.split( )[2:]
    status = ""

    for word in wordList:
      status = ' '.join(word)

    return status

  def __run_command_with_domain( command ):
    if self.domain is None:
      return

    this_subprocess = "{}{}".format(command, self.domain)

    try:
      subprocess.run(this_subprocess)
    except:
      exception_message = "An exception occurred."
      print(exception_message)