from Bash.BashCommand import *
from Bash.BashDatatype import *

text = BashCommand.GetInput()

expression =  "echo {}" \
              .format(text)

print(BashCommand.GetOutput(expression))