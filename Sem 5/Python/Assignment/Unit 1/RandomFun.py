import random

print("=== Demonstration of random module ===")

# Generate a random float between 0 and 1
print("Random float between 0 and 1:", random.random())

# Generate a random integer between two numbers
print("Random integer between 1 and 100:", random.randint(1, 100))

# Generate a random number from a range with a step
print("Random number from range 0 to 50 step 5:", random.randrange(0, 51, 5))

# Choose a random element from a list
colors = ['Red', 'Green', 'Blue', 'Yellow', 'Purple']
print("Random color:", random.choice(colors))

# Shuffle a list randomly
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled list:", numbers)

# Pick multiple random elements from a list
print("Pick 3 random colors:", random.sample(colors, 3))
