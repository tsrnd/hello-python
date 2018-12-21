
# Write
newFile = open("MyFile.txt", "w")    

newFile.write("Hello, python!\n")
newFile.write("Aww, I have new content!")

# Read
readFile = open("MyFile.txt", "r")

for line in readFile:
    print(line)

print(readFile.read())

# a list
print(readFile.readlines()) 