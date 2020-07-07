"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
import os
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
for arg in sys.argv:
    print(arg)

# Print out the OS platform you're using:
print("Current platform:", sys.platform)

# Print out the version of Python you're using:
print("Python version:", sys.version)


# OS module
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print("Current Process ID:", os.getpid())

# Print the current working directory (cwd):
print("Current working directory:", os.getcwd())

# Print out your machine's login name
print("Machine's login name:", os.getlogin())
