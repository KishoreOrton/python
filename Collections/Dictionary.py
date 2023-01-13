Dic = {1: "Kishore", 2: "Kumar", 3: "Latha"}
print(Dic)

Car = {
    "Company": "Maruthi",
    "Model": "Astar",
    "Year": 2010
}
# Print the value using KEY
print(Car["Company"])

# Get value using get function
print(Car.get("Year"))

# Change value using
Car["Model"] = "Astar VXI"
print(Car)

# Get only key the values
for i in Car:
    print(i)

# Get only values the values
for i in Car:
    print(Car[i])

# Get both key and values the values
for x, y in Car.items():
    print(x, y)

# Check the key

if "Model" in Car:
    print("YES")
else:
    print("NO")

# Add the values in the dic

Car["Insurance"] = "Current"
print(Car)

# Remove the items in the dic
Car.pop("Year")
print(Car)

del Car["Model"]
print(Car)

del Car
# print(Car)  # This will give name error since the dictionary is not presented

