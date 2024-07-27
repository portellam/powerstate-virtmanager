#!/usr/local/bin/python

import os
import subprocess
import sys

#
# Test bash input
#

command = "echo \"Hello World!\""
print(command)

# result = sys.stdin.readline(command)
# print("sys.stdin.readline")
# print("result == \"{}\"".format(result))
# print()

result = subprocess.check_output(
  command,
  shell = True,
)

print("subprocess.check_output")
print("result == \"{}\"".format(result))
print()

# result = subprocess.run(
#   command,
#   capture_output = True,  # Python >= 3.7 only
#   text = True             # Python >= 3.7 only
# )

# print("subprocess.run")
# print("result == \"{}\"".format(result))
# print()

result = os.system(command)               # returns code.
print("os.system")
print("result == \"{}\"".format(result))
print()

###

command = "sudo virsh list --all --name | head"
print(command)

result = subprocess.check_output(
  command,
  shell = True,
)

print("subprocess.check_output")
print("result == \"{}\"".format(result))
print()

# result = sys.stdin.readlines(command)
# print("sys.stdin.readlines")
# print("result == \"{}\"".format(result))
# print()

# result = subprocess.run(
#   command,
#   capture_output = True,  # Python >= 3.7 only
#   text = True             # Python >= 3.7 only
# )

# print("subprocess.run")
# print("result == \"{}\"".format(result))
# print()

result = os.system(command)               # returns code.
print("os.system")
print("result == \"{}\"".format(result))
print()
###