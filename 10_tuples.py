# Difference between Lists and Tuples

# List example
prime_numbers = [2, 3, 5, 7, 11, 13, 17]

# Tuple example
perfect_squares = (1, 4, 9, 16, 25, 36)

# Other than notation, there seems to be little difference between them.

# Display lengths - same for both
print("Display lengths:")
print("# Primes = ", len(prime_numbers))
print("# Squares = ", len(perfect_squares))

print("==============================")

# Iterate over both sequences - same for both
print("Iterate over both sequences:")
for p in prime_numbers:
    print("Prime: ", p)

for n in perfect_squares:
    print("Square: ", n)

print("==============================")

# Let's see the difference
print("List methods:")
print(dir(prime_numbers))
print(80*"-")
print("Tuple methods:")
print(dir(perfect_squares))

# We see that lists have more methods available, but they
# occupy more memory than tuples.

print("==============================")

import sys

print("Sys directory:")
print(dir(sys))
# print(help(sys.getsizeof))

list_eg = [1, 2, 3, "a", "b", "c", True, 3.14159]
tuple_eg = (1, 2, 3, "a", "b", "c", True, 3.14159)

print("List size = ", sys.getsizeof(list_eg))
print("Tuple size = ", sys.getsizeof(tuple_eg))

# Lists
# - Add data
# - Remove data
# - Change data

# Tuples
# - Cannot be changed (enables python to make significant optimizations)
# - Immutable
# - Mare more quickly than lists

print("==============================")

import timeit

print("Let's see how long it takes to create a million lists vs a million tuples.")

list_test = timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)
tuple_test = timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)

print("List time: ", list_test)
print("Tuple time: ", tuple_test)

print("==============================")

# Tuples use parentheses
empty_tuple = ()
test1 = ("a") # creates a string
test2 = ("a", "b")
test3 = ("a", "b", "c")
test4 = ("a",) # now it's a tuple

print(empty_tuple)
print(test1)
print(test2)
print(test3)
print(test4)

print("==============================")

# Alternative Construction of Tuples

test1 = 1,
test2 = 1, 2
test3 = 1, 2, 3

print(test1)
print(test2)
print(test3)

print(type(test1))
print(type(test2))
print(type(test3))

print("==============================")

# Tuples with 1 element
# Feature called Tuple Assignment

# (age, country, knows_python)
survey = (27, "Vietnam", True)

age = survey[0]
country = survey[1]
knows_python = survey[2]
print("Age = ", age)
print("Country = ", country)
print("Knows python? ", knows_python)

# Faster alternative
survey2 = (21, "switzerland", False)
age, country, knows_python = survey2
print("Age = ", age)
print("Country = ", country)
print("Knows python? ", knows_python)