def f():
    pass

f()

# this function doesn't show up on console bc it has no print statement
def ping1():
    return "Ping!"

def ping2():
    print("Ping!")

ping2()

print("=====================")
print("Solve for the volume of a sphere:")

import math
# We can now access pi:
# print(math.pi)

def volume(r):
    # This is a docstring - provides documentation on what the function does
    # and how to use it.
    """Returns the volume of a sphere with radius r."""
    v = (4.0/3.0) * math.pi * r**3
    return v

res = volume(3)
print(res)

# alternatively:
print(volume(2))

# help(volume)

print("=====================")
print("Compute the area of a triangle:")

def triangle_area(b, h):
    """Returns the area of a triangle with base b and height h."""
    return 0.5 * b * h

triangle_res = triangle_area(3,6)
print(triangle_res)

# alternatively:
print(triangle_area(4,5))

# Keyword Arguments (also called Default Arguments)

print("=====================")
print("Convert a length from feet and inches to centimeters.")

def cm(feet = 0, inches = 0):
    """Converts a length from feet and inches to centimeters."""
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm + feet_to_cm

# If you don't specify one of the keyword arguments, it's left on default
print(cm(feet = 5))
print(cm(inches = 70))
print(cm(feet = 5, inches = 8))
print(cm(inches = 8, feet = 5))

# Types of Arguments:
# Keyword and Required
# You can use both at the same time, but if you do that, 
# the keyword argument must come last.

print("=====================")
print("Types of Arguments")

# Keyword argument x is optional
def g(y, x = 0):
    return x + y

print(g(5))
print(g(7, x = 3))