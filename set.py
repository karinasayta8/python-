# Creating a set
fruits = {"apple", "banana", "cherry"}

# Adding an element
fruits.add("date")
print(f"After adding an element: {fruits}")

# Removing an element
fruits.remove("banana")
print(f"After removing an element: {fruits}")

# Discarding an element
fruits.discard("kiwi")  # Does nothing, since "kiwi" is not in the set
print(f"After discarding an element: {fruits}")

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
union_set = set1 | set2
print(f"Union of sets: {union_set}")

# Intersection
intersection_set = set1 & set2
print(f"Intersection of sets: {intersection_set}")

# Difference
difference_set = set1 - set2
print(f"Difference of sets: {difference_set}")

# Symmetric Difference
symmetric_difference_set = set1 ^ set2
print(f"Symmetric Difference of sets: {symmetric_difference_set}")

# Set Membership
print(f"Is 'apple' in fruits? {('apple' in fruits)}")
