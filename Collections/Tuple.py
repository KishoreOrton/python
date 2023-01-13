Tuple = ("Kishore", "Kumar")
print(Tuple)
print(Tuple[1])
print(Tuple[1:2])

# since it is immutable we cant change the value, but we can change tuple to list, and we can perform modification ,
# then we can change list to tuple again

List01 = list(Tuple)
# print(List01)
List01[1] = "Orton"
# print(List01)
Tuple = tuple(List01)
print("Modification from list to tuple", Tuple)

# Loop statement to read all the list items
for i in Tuple:
    print(i)

# Example check the item is in the list

if "Kishore" in Tuple:
    print("YES")
else:
    print("NO")
print("Length of the values", len(Tuple))

# Add value using list

List02 = list(Tuple)
# print(List01)
List02.append("KK")
# print(List02)
Tuple1 = tuple(List02)
print(Tuple1)

# Copy value using list
Tuple = Tuple1
print(Tuple)

