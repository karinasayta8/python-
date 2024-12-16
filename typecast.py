# Integer to float
num_int = 10
num_float = float(num_int)
print(f"Integer: {num_int}, After Typecasting to Float: {num_float}")

# Float to integer
num_float = 10.7
num_int = int(num_float)
print(f"Float: {num_float}, After Typecasting to Integer: {num_int}")

# Integer to string
num_int = 25
num_str = str(num_int)
print(f"Integer: {num_int}, After Typecasting to String: {num_str}")

# String to integer
num_str = "50"
num_int = int(num_str)
print(f"String: '{num_str}', After Typecasting to Integer: {num_int}")

# String to float
num_str = "15.5"
num_float = float(num_str)
print(f"String: '{num_str}', After Typecasting to Float: {num_float}")

# Implicit typecasting
result = 5 + 2.5  # Python automatically converts integer 5 to float
print(f"Result of Implicit Typecasting: {result} (Type: {type(result)})")
