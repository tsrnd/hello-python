import re

print(re.search("ahihi", "that should do ahihi it"))

print(re.split("[a-z]+", "i have 3 apple", flags=re.IGNORECASE))

print(re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "anh ngo").group('first_name'))

#sub function
n = "i think 0969696996 is the phone number in the board"
print(re.sub(r"\D", "", n))