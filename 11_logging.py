# Logging
# Purpose:
# Allows you to write status messages to a file or other output streams.
# These messages contain information on which parts of your code have
# executed, and what problems may have arisen.
# Levels:
# Five built-in levels: Debug, Info, Warning, Error, Critical

# Level     Numeric Value
# NOTSET    0
# DEBUG     10
# INFO      20
# WARNING   30
# ERROR     40
# CRITICAL  50

# Loggers will only write messages with a level greater than on equal to
# the set level.
# basicConfig: Default log level is WARNING = 30

import logging
# If you do dir(logging):
# All caps are constants, First letter capitalized are classes,
# items starting with lowercase letter are methods.
# Let's use the basicConfig method.

# Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "/home/belle/Development/PythonLearning/Lumberjack.log",
                                level = logging.DEBUG, 
                                format = LOG_FORMAT,
                                filemode = 'w')
# filemode = 'w' sets log file to be overwritten each time.
# By default it's set to append.

logger = logging.getLogger()

# Test the logger
logger.info("Our SECOND message.")

# Test messages
logger.debug("This is a harmless debug message.")
logger.info("Just some useful info.")
logger.warning("I'm sorry, but I can't do that, Dave.")
logger.error("Did you just try to divide by zero?")
logger.critical("The entire internet is down!!")

# Let's see it in action
import math

def quadratic_formula(a, b, c):
    """Return the solutions to the equation ax^2 + bx + c = 0."""
    logger.info("quadratic_formula({0}, {1}, {2})".format(a, b, c))

    # Compute the discriminant
    logger.debug("# Compute the discriminant")
    disc = b**2 - 4*a*c

    # Compute the two roots
    logger.debug("# Compute the two roots")
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)

    # Return the roots as a tuple
    logger.debug("# Return the roots as a tuple")
    return (root1, root2)

# Test by solving x^2 - 4 = 0
roots = quadratic_formula(1, 0, -4)
print(roots)

# x^2 + 1 = 0 gives errors
roots2 = quadratic_formula(1, 0, 1)
print(roots2)