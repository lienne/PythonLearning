# Fib Sequence:
# 1, 1, 2, 3, 5, 8, 13, 21, . . .

# Write a function to return the nth term of the Fibonacci Sequence.
# Function should be fast, clearly written, and rock solid.

def fibonacci_recursive(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    elif n > 2:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Super slow
for n in range(1, 2):
    print(n, ":", fibonacci_recursive(n))

# Memoization!
# 1. Implement explicitly
# 2. Use built-in python tool

# Dictionary to store recent function calls
fib_cache = {}

def fibonacci_memo(n):
    # If we have the cached value, then return it
    if n in fib_cache:
        return fib_cache[n]
    
    # Compute the Nth term
    if n == 1:
        value = 1
    if n == 2:
        value = 1
    elif n > 2:
        value = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    
    # Cache the value and return it
    fib_cache[n] = value
    return value

# Faster response
for n in range(1, 2):
    print(n, ":", fibonacci_memo(n))


from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):
    # If we have the cached value, then return it
    if n in fib_cache:
        return fib_cache[n]
    
    # Compute the Nth term
    if n == 1:
        value = 1
    if n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
    
    # Cache the value and return it
    fib_cache[n] = value
    return value

# Almost instantaneous response
for n in range(1, 2):
    print(n, ":", fibonacci_memo(n))

# Let's compute the ratio between consecutive terms in the sequence
for n in range(1, 51):
    print(fibonacci(n+1) / fibonacci(n))

# It converges to the Golden Ratio.