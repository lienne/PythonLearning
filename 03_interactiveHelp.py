# Interactive features help you quickly learn about classes,
# modules, functions, even when you are offline.

dir() # Short for directory
# Displays list of available objects

# __builtins__
#dir(__builtins__) <-- can only do this on interactive mode

#help(pow)
print(pow(2, 10))
print(2**10)

#help(hex)
print(hex(10))
print(0xa) # returns the decimal

# List of Modules
# help('modules')
# To learn about a module and see what objects are available,
# you must first import it.

import math
# dir() now shows 'math'
# dir(math)
# help(math.radians)

# radians(180) gives error
print(math.radians(180))