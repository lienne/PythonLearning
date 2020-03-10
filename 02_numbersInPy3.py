# There are 3 types of numbers in Python 3:
# int, float, complex

# int
a = 496
print(a)
print(type(a))

# float
e = 2.718281828
print(e)
print(type(e))

# complex
# Python stores the real and imaginary parts of complex numbers as floats
# Use j instead of i for the imaginary part (sqrt(-1))
z = 2 - 6.1j
print(z)
print(type(z))
print(z.real)
print(z.imag)

print('===========================')


# Operations: + - * /

# Any int value can also be represented by a float, but not the other way around
x = 28 # int
y = 28.0 # float, or
print(float(28))
# Not all floats can be converted to int
3.14 # float
print(int(3.14)) # gets printed as just 3
# ints are narrower than floats
# floats are wider than ints

# Any float can be made into a complex num, but not vice versa
x = 1.732 # float
1.732 + 0j # or
print(complex(1.732))
# floats are narrower than complex numbers
# complex numbers are wider than floats

# Arithmetic Operations

a = 2 # int
b = 6.0 # float
c = 12 + 0j # complex

# Rule: Widen numbers so they're the same type.
# Python will automatically convert the narrower to the wider type

# Addition
print(a + b) # int + float = float

# Subtraction
print(b - a) # float - int = float

# Mult
print(a * 7) # int * int = int

# Division
print(c / b) # complex / float = complex

# If you divide two whole numbers, it returns a float, 
# even if there is no remainder

print(16 % 5) # returns remainder

print(16 // 5) # returns only quotient

# you cannot divide by zero: throws ZeroDivisionError

print('===========================')


# Booleans
# Built in data type
# Logical type: only True or False
# Make sure to capitalize! Typing 'true' or 'false' returns an error.

a = 3
b = 5

print(a == b) # False
print(a != b) # True
print(a > b) # False
print(a < b) # True

print(type(True))

print('===========================')

print(bool(28))
print(bool(-2.718278))
print(bool(0)) # False

# Every other number besides 0 is converted to true.

print(bool("Turing"))
print(bool(" "))
print(bool("")) # False

# Every other string besides the empty string is converted to true.

# Rule:
# Trivial values     -> False
# Non-trivial values -> True

print('===========================')

print(int(True)) # gets converted to 1
print(int(False)) # gets converted to 0