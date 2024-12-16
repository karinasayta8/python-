# Create a list
fruits = ["apple", "banana", "cherry", "date"]

# Accessing elements
print("Accessing elements:")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print()

# Slicing a list
print("Slicing the list:")
print(f"First three fruits: {fruits[:3]}")
print(f"Fruits from index 2 onwards: {fruits[2:]}")
print()

# Adding elements
print("Adding elements:")
fruits.append("elderberry")  # Add at the end
print(f"After append: {fruits}")
fruits.insert(2, "fig")  # Insert at index 2
print(f"After insert: {fruits}")
print()

# Removing elements
print("Removing elements:")
fruits.remove("banana")  # Remove by value
print(f"After remove: {fruits}")
removed_fruit = fruits.pop(1)  # Pop element at index 1
print(f"Removed fruit: {removed_fruit}")
print(f"After pop: {fruits}")
print()

# List length
print(f"Length of the list: {len(fruits)}")
print()

# List Concatenation
more_fruits = ["grape", "honeydew"]
all_fruits = fruits + more_fruits  # Concatenation
print(f"Concatenated list: {all_fruits}")
print()

# Repetition
repeated_fruits = fruits * 2  # Repeat the list
print(f"Repeated list: {repeated_fruits}")
print()

# List comprehension
print("List comprehension (squares of numbers):")
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")
