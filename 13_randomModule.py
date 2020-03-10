# WARNING: The pseudo-random generators of this module should NOT be used
# for security purposes. Use os.urandom() or SystemRandom if you require
# a cryptographically secure pseudo-random number generator.

import random

# By default, the random() function in the random module
# returns a number in the interval [0,1).
# Display 10 random numbers from interval [0, 1)

for i in range(10):
    print(random.random())

print("======================================")

# Generate random numbers from [3, 7)?
# First way:
# Call random():                in [0,1)
# Scale number (multiply by 4): in [0,4)
# Shift number (add 3):         in [3, 7)

def my_random():
    # Random, scale, shift, return
    return 4*random.random() + 3

for i in range(10):
    print(my_random())

print("======================================")

# Easier way: Use the uniform function (in the random module)

for i in range(10):
    print(random.uniform(3, 7))

print("======================================")

# Normal Distribution random numbers (a.k.a. Bell Curve)
# use normalvariate() function, must pass in mean and standard deviation

for i in range(20):
    print(random.normalvariate(5, 0.2))

print("======================================")

# randint(min, max) function - "Random Integer", returns whole numbers

for i in range(10):
    print(random.randint(1, 6))

print("======================================")

# Random element from a list of values which are not numbers

outcomes = ['rock', 'paper', 'scissors']

for i in range(10):
    print(random.choice(outcomes))