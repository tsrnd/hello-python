import re

# search
abc = "Hello python!"
match = re.search("python!", abc)
if match is not None:
    print(match.group())

# match
abc = "django"
match = re.match(r'^d.*o$', abc)
if match is not None:
    print("Match!")

# full match
a = "abcd1234"
match = re.match(r'^[a-z0].*[0-9]$', a)
if match is not None:
    print("Match!")

# split
a = "abcd1234"
match = re.split(r'\d', a)
if match is not None:
    print(match)

# sub
a = "afsdldkjf1212lsdjfsldj"
b = re.sub(r'\d', '#', a)
print(b)
