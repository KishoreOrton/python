Set = {"Kishore", "Kumar", "kk"}
print(Set)

# Get values form the set

for i in Set:
    print(i)

Yesno = "Kumar" in Set
print(Yesno)

# adding items
Set.add("Latha")  # adding Single value
print(Set)

Set.update("M", "N")  # adding Multiple value
print(Set)
print(len(Set))     # Length

# Remove item from set
Set.remove("M")     # Throws error if u give wrong value
print(Set)

Set.discard("N")    # Won't Throw error if u give wrong value
print(Set)

# Clear all itmes
Set1 = {"Kishore", "Kumar", "kk"}
Set1.clear()
print(Set1)

# Combine 2 sets
Set01 = {1,2,3,4}
Set02 = {5,6,7}
print(Set01.union(Set02))

# Update function
Set01.update(Set02)
print(Set01)

