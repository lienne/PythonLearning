# Write function to compute 3x + 1

def f(x):
    return 3*x + 1
print(f(2))

# In Lambda:
lambda x: 3*x + 1

# You can still give it a name and use it normally:
g = lambda x: 3*x + 1
print(g(3))

# Lambda Expressions with multiple inputs
# Combine first and last names into a single "Full Name"

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("    leonhard", "EULER"))

print(40*"=")

# A function with no name:
# Let's sort this list by last names.
scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", 
"Arthus C. Clarke", "Frank Herbert", "Orson Scott Card", "Douglas Adams", 
"H. G. Wells", "Leigh Brackett"]

# help(scifi_authors.sort)

# Make anonymous function to pass as the key argument in the sort method.
# To access last name, split the string into pieces wherener it has a space.
# Access last piece by index -1.
# Convert the string to lowercase (so sorting isn't case-sensitive)
scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_authors)

print(40*"=")

# Function that makes functions
# Quadratic Functions
def build_quad_func(a, b, c):
    """Returns the function f(x) = ax^2 + bx + c"""
    return lambda x: a*x**2 + b*x + c

f = build_quad_func(2, 3, -5)
print(f(0))
print(f(1))
print(f(2))

print(build_quad_func(3, 0, 1)(2)) # 3x^2 + 1 at x = 2