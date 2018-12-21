f = open("hello-python/text.txt", "r")
# print(f.read())
# print(f.read())
# f.close
try:
    print(f.readline())
except FileNotFoundError:
    print("file not found")
# for x in f:
#     print(x)
# f = open("hello-python/text.txt", "w")
# f.write("Woops! I have deleted the content!")

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

import unittest
if __name__ == "__main__":
    import test_module
    test_module.TestStringMethods