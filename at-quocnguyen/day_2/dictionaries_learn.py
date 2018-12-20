# Tương tự như list
# Có thể coi như cấu trúc Json gồm key and value


info_of_me = {"name":"quoc", "company": "asiantech", "team": "android"}

name = info_of_me["name"]
print (name)
# adding item
things_to_remember = {
    0: "the lowest number",
    "a dozen" : 12,
    "snake eyes": "a pair of ones",
    13: "a baker 's dozen",
}

print (things_to_remember[0])

# remove item  used del


# for loop
for each_value in things_to_remember.values():
    print ("value of dict: ", each_value)

for each_key in things_to_remember.keys():
    print("key of dict: ", each_key)

# Create list of dict

customers = [
    {
        "id": 0,
        "name": "John",
    },
    {
        "id": 1,
        "name": "Kaka",
    },
    {
        "id": 2,
        "name": "Mes",
    },
]

print (customers)
print (customers[2]["name"])

# Create list inside of dict

customer1 = {
    "id": 4,
    "name": "quoc",
    "info": ["asiantech", "android"],
}

customers.append(customer1)

print (customers)