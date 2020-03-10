print("Example 1:")

example = set()
# dir(example)

# Think hashset: Duplicates are not stored.
# A duplicate is ignored.
# For sets, the order does NOT matter.

example.add(42)
example.add(False)
example.add(3.14159)
example.add("Thorium")

print(example)

example.add(42)
print(example)
print(len(example))

example.remove(42)
print(example)
print(len(example))

# example.remove(50) # returns error (sometimes helpful)

example.discard(50)

print("========================")
print("Example 2:")

example2 = set([28, True, 2.71828, "Helium"])
print(len(example2))
example2.clear()
print(len(example2))

# Union and Intersection of Sets

print("========================")
print("Union and Intersection of Sets")

# Integers 1 - 10
odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composite = set([4, 6, 8, 9, 10]) # integers that can be factored

print(odds.union(evens))
print(evens.union(odds))
print(odds.intersection(primes))
print(primes.intersection(evens))
print(evens.intersection(odds)) # empty set
print(primes.union(composite))

# Testing to see if one element is inside a set
print(2 in primes)
print(6 in odds)
print(9 not in evens)

# dir(primes)