print("hello")

xs = [()]
res = [False] * 2
if xs:
    res[0] = True
if xs[0]:
    res[1] = True
print(res)

if True:
    print(True)
else:
    print(False)

word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is 
made up of multiple lines and sentences."""
print(paragraph)

# print("Enter your name: ")
# x = input()
# print("Hello, " + x)

for x in range(10, 0, -1):
  print(x)