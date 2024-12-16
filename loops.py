# Demonstrating loops in Python

# For loop: Print numbers from 1 to 5
print("For loop:")
for i in range(1, 6):
    print(i, end=" ")
print("\n")

# While loop: Print numbers from 1 to 5
print("While loop:")
count = 1
while count <= 5:
    print(count, end=" ")
    count += 1
print("\n")

# Nested loop: Print a multiplication table from 1 to 3
print("Nested loop: Multiplication table")
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"{i} x {j} = {i * j}")
    print()  # Blank line after each table
