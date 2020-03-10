# You live in a perfect grid. When you go for a walk, at each intersection
# you choose your next direction randomly.
# Your four choices are north, east, south, and west.
# Backtracking is permitted.
# Once you are finished, you check to see how far away you are from home.
# If you are more than 4 blocks away, you need to pay for transport back.
# Otherwise, you can just walk back.

# What is the longest random walk you can take from home so that on average
# you will end up 4 blocks or fewer from home?

# The Plan
# - Write random walk function
# Version 1 - Simple and clear, from scratch
# Version 2 - Use python shortcuts to cut the length

import random

def random_walk(n):
    """Return coordinates after 'n' block random walk."""
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N', 'S', 'E', 'W'])
        if step == 'N':
            y = y + 1
        elif step == 'S':
            y = y - 1
        elif step == 'E':
            x = x + 1
        else:
            x = x - 1
    return (x,y)

# Test function by taking 25 random walks, each 10 blocks long
for i in range(25):
    walk = random_walk(10)
    print(walk, "Distance from home = ", abs(walk[0]) + abs(walk[1]))

print(40*"=")

# Version 2 - shorter
def random_walk2(n):
    """Return coordinates after 'n' block random walk."""
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x, y)

for i in range(25):
    walk = random_walk2(10)
    print(walk, "Distance from home = ", abs(walk[0]) + abs(walk[1]))


# Monte Carlo method
# Conduct thousands of random trials and compute the percentage of random
# walks that end in a short walk home.

number_of_walks = 10000

# Let's estimate the probability that you'll walk home for walks of
# length 1 to 30 blocks
for walk_length in range(1, 31):
    # Keep track of number of random walks that end 4 blocks or fewer from home
    no_transport = 0 # number of walks 4 or fewer blocks from home

    # Monte Carlo loop of 10,000 samples
    for i in range(number_of_walks):
        (x, y) = random_walk2(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    
    # Compute % of random walks that ended with a walk home
    no_transport_percentage = float(no_transport) / number_of_walks

    print("Walk size = ", walk_length, " / % of no transport = ", 100*no_transport_percentage)