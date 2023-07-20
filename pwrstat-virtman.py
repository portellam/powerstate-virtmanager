from os import system

# <params>
STATE_PAUSED    = "paused"
STATE_STARTED   = "running"
STATE_STOPPED   = "shut off"
STATE_SUSPENDED = "pmsuspended"

COMMAND_PREFIX  = "sudo virsh"

OPTION_LIST_ALL       = "list --all"
OPTION_PAUSE_RESUME   = "resume"
OPTION_PAUSE_STOP     = "suspend"
OPTION_PAUSE_SUSPEND  = "dompmwakeup"
OPTION_SET_DOMAIN     = "--domain"
OPTION_SET_TARGET     = "--target"
OPTION_START          = "start"
OPTION_STOP           = "shutdown"
OPTION_TARGET_BOTH    = "hybrid"
OPTION_TARGET_DISK    = "disk"
OPTION_TARGET_RAM     = "mem"

GET_UNFILTERED_DOMAIN_LIST      = "{} {} | grep -Eiv 'Id|Name|State' | cut -d '-' -f 2 | cut -d ' ' -f 5 | grep -Ei [A-Za-z] )".format(COMMAND_PREFIX,OPTION_LIST_ALL)
GET_UNFILTERED_DOMAIN_AND_STATE = "{} {} | grep '$DOMAIN' | head -n 1 | awk 'END {print $2}'".format(COMMAND_PREFIX,OPTION_LIST_ALL)

SET_SUSPEND_DOMAIN_TO_DISK_ONLY     = "{} {} {} {} ".format(COMMAND_PREFIX,OPTION_SET_TARGET,OPTION_TARGET_DISK,OPTION_SET_DOMAIN)
SET_SUSPEND_DOMAIN_TO_DISK_AND_RAM  = "{} {} {} {} ".format(COMMAND_PREFIX,OPTION_SET_TARGET,OPTION_TARGET_BOTH,OPTION_SET_DOMAIN)
SET_SUSPEND_DOMAIN_TO_RAM_ONLY      = "{} {} {} {} ".format(COMMAND_PREFIX,OPTION_SET_TARGET,OPTION_TARGET_RAM,OPTION_SET_DOMAIN)
# </params>

# <functions>
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
# </functions>

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
