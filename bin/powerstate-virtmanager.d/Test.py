import BashCommand
import BashDatatype

text = BashCommand.get_command_input()

expression =  "echo {}" \
              .format(text)

print(BashCommand.get_command_output(expression))