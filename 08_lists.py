# Lists preserve order, while sets don't.

example_constructor = list()
example = []

primes = [2, 3, 5, 7, 11, 13]
print(primes)
primes.append(17)
primes.append(19)
print(primes)

print(primes[0])
print(primes[1])

# You can wrap around in python ONCE
print(primes[-1]) # last item in the list
print(primes[-2]) # second-to-last item in the list
print(primes[-8]) # takes us back to the first item on the list

# You can only wrap around once, so this gives an error
# print(primes[-9])

# Slicing - makes a sublist

# beginning value is included, ending value is not
print(primes[2:5])
print(primes[0:6])

# Lists can also contain duplicate values.
# There can even be lists within a list.
example = [128, True, "Alpha", 1.732, [64, False]]

# Lists can also contain duplicate values
rolls = [4, 7, 2, 7, 12, 4, 7]

# You can also combine lists (concatenation)
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
# Order matters
print(numbers + letters)
print(letters + numbers)

numbers.reverse()
print(numbers)