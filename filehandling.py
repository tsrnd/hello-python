f = open("hello-python/text.txt", "r")
# print(f.read())
# print(f.read())
# f.close
print(f.readline())
for x in f:
    print(x)
f = open("hello-python/text.txt", "w")
f.write("Woops! I have deleted the content!")