# Creating a tuple
fruits = ("apple", "banana", "cherry")

# Accessing tuple elements
print("Accessing elements:")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print()

# Slicing the tuple
print("Slicing the tuple:")
print(f"First two fruits: {fruits[:2]}")
print(f"Fruits from index 1 onwards: {fruits[1:]}")
print()

# Concatenating tuples
more_fruits = ("date", "elderberry")
all_fruits = fruits + more_fruits
print(f"Concatenated tuple: {all_fruits}")
print()

# Repeating tuple
repeated_fruits = fruits * 2
print(f"Repeated tuple: {repeated_fruits}")
print()

# Length of tuple
print(f"Length of the tuple: {len(fruits)}")
