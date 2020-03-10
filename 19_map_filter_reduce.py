# Map, Filter, Reduce functions

import math

def area(r):
    """Area of a circle with radius 'r'."""
    return math.pi * (r**2)

# What if we need to compute the areas for many different circles?
radii = [2, 5, 7.1, 0.3, 10]

# Method 1: Direct
areas = []
for r in radii:
    a = area(r)
    areas.append(a)
print(areas)

# Method 2: Map function
# map takes two arguments: first is a function, second is your list, tuple,
# or other iterable object.
map(area, radii) # returns map object
print(list(map(area, radii)))

print(40*"=")

# Converting temperature from Celsius to Farenheit
temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19), 
    ("Los Angeles", 26), ("Tokyo", 27), ("New York", 28), ("London", 22),
    ("Beijing", 32)]

c_to_f = lambda data: (data[0], (9/5)*data[1] + 32)

print(list(map(c_to_f, temps)))

print(40*"=")

# Filter Function
# Example: Finda all data above the average.

import statistics

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print(avg)

# First arg is a function
filter(lambda x: x > avg, data) # returns filter object
# Above avg:
print(list(filter(lambda x: x > avg, data)))
# Below avg:
print(list(filter(lambda x: x < avg, data)))

# Remove missing data
countries = ["", "Argentina", "", "Brazil", "Chile", "", "Colombia", "",
    "Ecuador", "", "", "Venezuela"]
# filters out all values that are treated as false in a boolean setting:
print(list(filter(None, countries)))

# In python, the values that are treated as false are:
# "", 0, 0.0, 0j, [], (), {}, False, None, and 
# instances of objects which signal they are empty (trivial instances)
# Be careful when using the filter function in this way:
# 0 is a valid piece of data in most situations, so you would not want
# to filter that out.

print(40*"=")

# Reduce function
# In Python3+. reduce is no longer a built-in function.
# It has been demoted to the 'functools' module.
# Use functools.reduce() if you really need it; however, 99% of the time 
# an explicit for loop is more readable.

# Example: Multiply all numbers in a list

from functools import reduce

data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
multiplier = lambda x, y: x*y
print(reduce(multiplier, data))

# Using a for loop:
product = 1
for x in data:
    product = product * x
print(product)

