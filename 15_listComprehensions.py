# List: [1, 2, "a", 3.14]
# List Comprehensions:
#       [expr for val in collection]
#       [expr for val in collection if <test>]
#       [expr for val in collection if <test1> and <test2>]
#       [expr for val1 in collection1 and val2 in collection2]

# Example: List of Squares

# Without list comprehension
squares = []
for i in range(1, 101):
    squares.append(i**2)
print("Squares list:")
print(squares)

print(40*"=")

# With list comprehension
squares_comp = [i**2 for i in range(1, 101)]
print("Squares list comprehension:")
print(squares_comp)

print(40*"=")

# Example: Remainders when you divide the first 100 squares by <5, 11>
remainders5 = [x**2 % 5 for x in range(1, 101)]
print("Remainders of 5 list:")
print(remainders5)
# There are only three perfect squares mod 5: 0, 1, and 4

print(40*"=")

remainders11 = [x**2 % 11 for x in range(1, 101)]
print("Remainders of 11 list:")
print(remainders11)
# The perfect squares mod 11 are: 0, 1, 3, 4, 5, 9

print(40*"=")

# Sorting list of movies

movies = ["Star Wars", "Gandhi", "Casablanca", "Shawshank Redemption", 
"Toy Story", "Gone With the Wind", "Citizen Kane", "It's a Wonderful Life", 
"The Wizard of Oz", "Gattaca", "Rear Window", "Ghostbusters", "To Kill a Mockingbird", 
"Good Will Hunting", "2001: A Space Odyssey", "Raiders of the Lost Ark", 
"Groundhog Day", "Close Encounters of the Third Kind"]

# With simple List
gmovies = []
for title in movies:
    if title.startswith("G"):
        gmovies.append(title)
print(gmovies)

# With List Comprehension
gmovies2 = [title for title in movies if title.startswith("G")]
print(gmovies2)


print(40*"=")

# Scalar Multiplication
print("Scalar Multiplication")
v = [ 2, -3, 1]
print(4*v) # returns a list containing four copies of v
# If you add lists, they get concatenated

w = [4*x for x in v]
print(w)


print(40*"=")

# Cartesian Product of Sets
# For sets A and B, A x B = (a, b) for a in A and b in B
print("Cartesian Product of Sets")
A = [ 1, 3, 5, 7]
B = [2, 4, 6, 8]

cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)