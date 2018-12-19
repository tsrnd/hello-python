thisdict = {
    "name": "Na",
    "age": 23
}
print(thisdict)
print(thisdict["name"])
print(thisdict.get("name"))
thisdict["name"] = "A"
print(thisdict)
for x in thisdict:
    print(x)
for y in thisdict:
    print(thisdict[y])
for z in thisdict.values():
    print(z)
for t, k in thisdict.items():
    print(t, k)
if "name" in thisdict:
    print("name is one of the keys in the thisdict dictionary")
print(len(thisdict))

thisdict["address"] = "Da Nang"
print(thisdict)

thisdict.pop("address")
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict["name"]
print(thisdict)

thisdict = dict(name="Na", age=23)
print(thisdict)

thisdict.clear()
print(thisdict)
