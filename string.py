name = input('Enter your name: ')
print(name * 3)
print(name[0])
print(name[-1])


print(name.upper())
print(name.lower())
print(name.find('Rina'))

s = "Python"
print(s[0:3])  # Output: "Pyt" (characters from index 0 to 2)
print(s[2:])   # Output: "thon" (from index 2 to the end)
print(name.replace("ka","sa"))
print(len(name))
if(name.isalnum()):
    print("yes")

# Check membership
print("kar" in name)
print("kar" not in name)
    
# string formatting
print(f"my name is {name}")
print("My name is {}".format(name))


# split function
s = "Hello Python World"
result = s.split(" ")
print(result)
