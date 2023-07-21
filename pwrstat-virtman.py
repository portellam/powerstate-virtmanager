from os import system

class DomainModel:
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
  option_target_memory     = "mem"

  state_paused    = "paused"
  state_started   = "running"
  state_stopped   = "shut off"
  state_stop      = "pmsuspended"

  get_unfiltered_domain_list      = "{} {} | grep -Eiv 'Id|Name|State' | cut -d '-' -f 2 | cut -d ' ' -f 5 | grep -Ei [A-Za-z] )".format(command_prefix,option_list_all)
  get_unfiltered_domain_and_state = "{} {} | grep '$DOMAIN' | head -n 1 | awk 'END {print $2}'".format(command_prefix,option_list_all)

  set_hard_start_domain   = "{} {} ".format(command_prefix,option_hard_start)
  set_hard_stop_domain    = "{} {} ".format(command_prefix,option_hard_stop)

  set_power_start_domain                    = "{} {} ".format(command_prefix,option_power_start)
  set_power_stop_domain_to_disk             = "{} {} {} {} ".format(command_prefix,option_set_target,option_target_disk,option_set_domain)
  set_power_stop_domain_to_disk_and_memory  = "{} {} {} {} ".format(command_prefix,option_set_target,option_target_both,option_set_domain)
  set_power_stop_domain_to_memory           = "{} {} {} {} ".format(command_prefix,option_set_target,option_target_memory,option_set_domain)

  set_soft_start_domain = "{} {} ".format(command_prefix,option_soft_start)
  set_soft_stop_domain  = "{} {} ".format(command_prefix,option_soft_stop)

  def __init__(self, domain):
    self.domain = domain

  def get_filtered_domain_name( line ):
    if line is None:
      return ""

    return line.split( )[1]

  def get_filtered_domain_state( line ):
    if line is None:
      return ""

    wordList = line.split( )[2:]
    status = ""

    for word in wordList:
      status = ' '.join(word)

    return status

  def run_command_with_domain( command ):
    if self.domain is None:
      return

    this_subprocess = "{}{}".format(command, self.domain)

    try:
      subprocess.run(this_subprocess)
    except:
      exception_message = "An exception occurred."
      print(exception_message)

  def do_hard_start_domain():
    run_command_with_domain(set_hard_start_domain)

  def do_hard_stop_domain( domain ):
    run_command_with_domain(set_hard_stop_domain)

  def do_soft_start_domain( domain ):
    run_command_with_domain(set_soft_start_domain)

  def do_soft_stop_domain( domain ):
    run_command_with_domain(set_soft_stop_domain)

  def do_power_stop_domain_to_disk( domain ):
    run_command_with_domain(set_power_stop_domain_to_disk)

  def do_power_stop_domain_to_disk_and_memory( domain ):
    run_command_with_domain(set_power_stop_domain_to_disk_and_memory,)

  def do_power_stop_domain_to_memory( domain ):
    run_command_with_domain(set_power_stop_domain_to_memory)

  # def parse_arguments( f ):
  #     def wrapper(something, argumentStr ):
  #         argumentList={ 0: f.__name__ }
  #         index=0

  #         for argument in argumentStr.split():
  #             index+=1

  #             if index>0 and '=' in argument:
  #                 argumentList[i] = argument.split('=', 1)

  #             else:
  #                 argumentList[i] = a

  #         return f(something, argumentList)
  #       wrapper.__doc__ = f.__doc__
  #   return wrapper

  # @parseargs

  # def do_set_variable_for_group(self, argumentList):
  #     'setvar_for_group <group> <var1=value1> : Sets a variable for a group'

  #     command = argumentList[0]   # command = 'setvar_for_group'
  #     group = argumentList[1]     # group = 'example_group'
  #     var_key = argument[2][0]    # var_key = 'myvar'
  #     var_value = argument[2][1]  # var_value = 'example'

  # #
  # # You would get this values by executing:
  # # prompt> setvar_for_group example_group myvar=example
