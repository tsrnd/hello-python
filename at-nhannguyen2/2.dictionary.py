# create dictionary
profile = {"Name": "Nguyen Nhan", "Age": 23}
print(profile)

# update key if key exist
profile["Age"] = 20
print(profile)

# create key if key not exist
profile["Company"] = "Asiantech"
print(profile)

# delete key if key exist
del profile["Company"]
print(profile)

# get all key
print(profile.keys())

# remove all key
profile.clear()
print(profile)


# delete dictionary
del profile
