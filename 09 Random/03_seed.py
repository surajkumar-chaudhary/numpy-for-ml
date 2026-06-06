import numpy as np

np.random.seed(2)

print(np.random.randint(1, 10, size=5))
print(np.random.randint(1, 10, size=5))

# Challenge

# Without running:

# np.random.seed(42)

# print(np.random.randint(1,10,size=5))
# print(np.random.randint(1,10,size=5))

# Will the two outputs be:

# A) Always identical

# B) Different

# Think carefully.

# The seed is set only once. 🤔

# A) Always identical

# This is a very common misunderstanding. 😊

# The answer is actually:

# B) Different

# Let's see why.

# np.random.seed(42)

# print(np.random.randint(1,10,size=5))
# print(np.random.randint(1,10,size=5))
# What seed does
# np.random.seed(42)

# resets the random number generator once.

# Think of it like:

# Start reading a book from page 1.
# First call
# np.random.randint(1,10,size=5)

# reads the first 5 random numbers.

# Example:

# [7 4 8 5 7]
# Second call
# np.random.randint(1,10,size=5)

# continues from where it left off.

# Example:

# [3 7 8 5 4]

# Different numbers.

# When would they be identical?

# If you reset the seed again:

# np.random.seed(42)
# print(np.random.randint(1,10,size=5))

# np.random.seed(42)
# print(np.random.randint(1,10,size=5))

# Now both outputs will be identical because you're restarting from the same point each time.

# Memory Trick
# seed()
# ↓
# Reset random generator
# Random call #1
# ↓
# Consumes numbers
# Random call #2
# ↓
# Continues from next numbers
# Challenge

# Without running:

# np.random.seed(100)

# a = np.random.randint(1,10,size=5)

# np.random.seed(100)

# b = np.random.randint(1,10,size=5)

# Will:

# a == b

# be:

# True
# or
# False

# ? 🤔

# True