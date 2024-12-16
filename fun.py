# Defining a function that takes parameters and returns a value
def greet(name):
    """This function greets the person passed as a parameter."""
    return f"Hello, {name}!"

# Calling the function
name = input("Enter your name: ")
greeting = greet(name)
print(greeting)

# Function with multiple parameters
def add(a, b):
    """This function adds two numbers."""
    return a + b

# Calling the function with arguments
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = add(num1, num2)
print(f"The sum of {num1} and {num2} is {result}")

# Function with a default argument
def greet_with_default(name="Guest"):
    """This function greets the person, or defaults to 'Guest'."""
    return f"Hello, {name}!"

# Calling the function with and without an argument
print(greet_with_default())  # Using default
print(greet_with_default("Alice"))  # Passing an argument

# Function with variable-length arguments (*args and **kwargs)
def print_values(*args, **kwargs):
    """This function prints variable number of positional and keyword arguments."""
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# Calling the function
print_values(1, 2, 3, name="John", age=25)
