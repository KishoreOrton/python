import keyword

# Prints all the keywords in the python
print(keyword.kwlist)

x = 10
y = 'kishore'
z = True
n = 'a'

# Datatype of X and Y
print(type(x))
print(type(y))
print(type(z))
# Data type for an is str in java its char
print(type(n))

# print multiple variables
print(x, y, z, n)

# Assign multiple variables
a, b, c = 10, 20, 'Hello'
print(a)
print(c)
print(a, b, c)

# Same value in variables
t = y = u = 10
print(t)
print(y)

# Interchange value in variables
x = 5
y = 20

x, y = y, x
print(y)
print(x)

# value in variables change
x = 100
print(x)
x = 500
print(x)

#  variables deletion
x = 100
print(x)
del x
print(x)