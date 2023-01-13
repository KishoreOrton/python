str1 = "KishoreKumar"
str2 = 'name'
str3 = str("name")

print(str1, str2, str3)

# Empty string
print("-----Empty string-----")
str4 = ""
str5 = ''
str6 = str("")

print("Empty string", str4, str5, str6, "Empty")

str7 = id(str1)
print(str7)

# + and * in strings
print("----- + and * in strings -----")

print(str1 + str2)
print(str1 * 5)

# Slicing string
print("-----Slicing string-----")

print(str1[1:4])
print(str1[:4])  # First 4 words
print(str1[7:12])  # Slice word
print(str1[1])  # Single char
print(str1[1:-1])  # Last char

# ASCII string
print("-----ASCII string-----")

print(ord("A"))
print(chr(70))

# Max()  Min() len()
print("-----Max()  Min() len()-----")

print(max("ABCDEFG"))
print(min("ABCDEFG"))
print(len("ABCDEFG"))

# In and not operator
print("-----In and not operator-----")
s = "welcome"
print("come" in s)
print("kome" in s)
print("come" not in s)
print("kome" not in s)

# String Comparison
print("-----String Comparison-----")
print("Geek" == "Geek")
print("Geek" < "geek")
print("Geek" > "geek")
print("Geek" != "Geek")
