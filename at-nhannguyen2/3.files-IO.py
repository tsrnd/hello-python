import os

# change directory
os.chdir("at-nhannguyen2")

# open file
files = open("file.txt", "w+")

# get file name
print(files.name)

# write file
files.write("python is great!\n")

# read file: read(count) count is byte read
print(files.read(10))

# check file if closed
print(files.closed)

# close file
files.close()

files = open("file2.txt", "wb")

# rename file
os.rename("file2.txt", "changename.txt")

# remove file
os.remove("changename.txt")
