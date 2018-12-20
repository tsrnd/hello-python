remmemberOfContent = """
    - w is a write on files
    - r only read content of files 
    - a append or write content

"""

print (remmemberOfContent)

with open ("greet.txt", "w") as f:
    f.write("I write something is beter")

with open ("greet.txt", "r") as f:
    text_of_file = f.read()
    print ("Just reading a file ", text_of_file)

with open("greet.txt", "a")  as f:
    f.write(" Have nice day")

with open ("greet.txt", "r") as f:
    text_of_file = f.read()
    print ("Just append a file ", text_of_file)