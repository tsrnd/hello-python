# =============================== Example about Array ===============================
fruits = ["apple", "banana", "cherry"]

# Print the second item in the fruits list.
print(fruits[1])

# Change the value from "apple" to "kiwi", in the fruits list.
fruits[0] = "kiwi"

# Use the append method to add "orange" to the fruits list.
fruits.append("orange")

# Use the insert method to add "lemon" as the second item in the fruits list.
fruits.insert(1, "lemon")

# Use the remove method to remove "banana" from the fruits list.
fruits.remove("banana")

# Remove the first item in the fruits list.
fruits.remove(fruits[0])

# Remove the last item in the fruits list.
fruits.remove(fruits[len(fruits)-1])

# display all fruits
print(fruits)


# =============================== Example about Tuples ===============================
# Tuples - Array readonly.
fruitsTuples = ("apple", "banana", "cherry")
# Another way:    fruitsTuples = tuple(("apple", "banana", "cherry"))

# Print the first item in the fruits tuple.
print(fruits[0])
# Print the number of items in the fruits tuple.
print(len(fruits))
# Check if "apple" is present in the tuple:
if "apple" in fruitsTuples:
    print("Yes, 'apple' is in the fruits tuple")

# using index and count
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)  # return index of value
print(thistuple.count(8))  # return times display of value.

# =============================== Example about Sets ===============================
# Create sets.
thisset = {"apple", "banana", "cherry"}
# Another way: thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# Add item to set.
thisset.add("tomato")
# using update if have more item added.
thisset.update(["orange", "mango", "grapes"])
# update twice for check conflict.
thisset.update(["orange", "mango"])
print('Sets after inserted: ', thisset)

# If the item to remove does not exist, it will raise an error
thisset.remove("banana")
# Remove item
thisset.discard("banana")

# Remove last item
thisset.pop()
# remove all items
thisset.clear()
# delete set
del thisset

# =============================== Example about Dictionary ===============================
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}  # Another way : dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)
x = thisdict.get("model")  # thisdict["model"]

# Display key and value
for x in thisdict:
    print(thisdict.get(x))
# Another way
for x, y in thisdict.items():
    print(x, y)

# Display values:
for val in thisdict.values():
    print(val)

#Copy data.
newDic = thisdict.copy()

# The pop() method removes the item with the specified key name:
thisdict.pop("model")
# Remove the last insert item
thisdict.popitem()
# Delete item with key
del thisdict["brand"]

print(newDic)