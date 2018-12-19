thistuples = ("apple", "orange", "banana")
print(thistuples)
print(thistuples[1])
thislist = list(thistuples)
print(thislist)
thislist[1] = "cherry"
del thislist[0]
tuples = tuple(thislist)
print(tuples)
for x in thistuples:
    print(x)
if "apple" in thistuples:
    print("apple is in thistuples")
print(len(thistuples))
print(thistuples.count("apple"))
print(thistuples.index("orange"))
