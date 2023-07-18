from os import system

STATE_ACTIVE = "running"
STATE_INACTIVE = "shut off"
STATE_PAUSE = "paused"
STATE_SUSPEND = "pmsuspended"

class BashLogic:
  command = "sudo virsh"
  command_list_all = "{} list --all".format(command)

  command_pause = "suspend".format(command)
  command_shutdown = "shutdown".format(command)
  command_start = "start".format(command)
  command_suspend = "dompmsuspend".format(command)
  command_resume_from_pause = "resume".format(command)
  command_resume_from_suspend = "dompmwakeup".format(command)

  option_set_target="--target"
  option_set_domain="--domain"

  get_unfiltered_domain_list = "{} | grep -Eiv 'Id|Name|State' | cut -d '-' -f 2 | cut -d ' ' -f 5 | grep -Ei [A-Za-z] )".format(command_list_all)
  get_unfiltered_domain_and_state="{} | grep '$DOMAIN' | head -n 1 | awk 'END {print $2}'".format(command_list_all)

  set_suspend_domain_to_disk="{} {} disk {} ".format(command_suspend, option_set_target, option_set_domain)
  set_suspend_domain_to_disk_and_ram="{} {} hybrid {} ".format(command_suspend, option_set_target, option_set_domain)
  set_suspend_domain_to_ram="{} {} mem {} ".format(command_suspend, option_set_target, option_set_domain)

  # def get_unfiltered_line( line ):

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
