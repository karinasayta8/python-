# Creating a dictionary
person = {"name": "John", "age": 30, "city": "New York"}

# Accessing values
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")

# Modifying a value
person["age"] = 31
print(f"Updated Age: {person['age']}")

# Adding a new key-value pair
person["job"] = "Engineer"
print(f"Updated Dictionary: {person}")

# Removing an item
removed_city = person.pop("city")
print(f"Removed city: {removed_city}")
print(f"Updated Dictionary: {person}")

# Iterating through the dictionary
print("\nDictionary contents:")
for key, value in person.items():
    print(f"{key}: {value}")
