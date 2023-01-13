List1 = [10, 20, 30, 40]
List2 = ["Kishore", "Kumar"]  # index start from 0
List3 = [10, "Kishore", 20, "Kumar"]
List4 = []  # Empty List

print(List1, List2, List3, List4)

print(List2[0])  # Get a particular value
print(List2[-1])  # Get a last value

# Range of index
print(List3[1:4])
print(List3[1:-1])

# Change item / value in the list
List2[1] = "Orton"
print(List2)

# Loop statement to read all the list items
for i in List3:
    print(i)

# Example check the item is in the list

if "Kumar" in List3:
    print("YES")
else:
    print("NO")

# Length of the list
length = len(List3)
print(length)

# Add items to the list
List1.append(60)  # Added end of the list
print(List1)

List1.insert(3, 35)  # Added in the index of the list (index , Value)
print(List1)

# Remove items to the list
List1.pop(0)  # pop() remove by index
print(List1)

del List1[2]  # del Variable remove by index
print(List1)

List1.clear()
print(List1)

# Copy items to the list
MyList1 = [10, 20, 30, 40]     # List
MyList2 = list(MyList1)
print(MyList2)

MyList3 = MyList1.copy()
print(MyList3)

# Combine/Join items to the list
for i in List3:
    List2.append(i)
print(List2)

List2.extend(List3)
print(List2)

L
