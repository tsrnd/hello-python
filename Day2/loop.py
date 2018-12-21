# For

def forInRange():
    for i in range(6):
        print(i)

forInRange()

def forAllElement():
    arr = [1,2,3,4,5,6,7,1,2,3,5,6,7]
    for index, value in enumerate(arr):
        print('Index: %d Value: %d' %(index, value))

forAllElement()

# Nested Loop

def nestedLoop():
    adj = ["red", "big", "tasty"]
    fruits = ["apple", "banana", "cherry"]
    for x in adj:
        for y in fruits:
            print(x, y)

nestedLoop()

# While
def whileLoop():
    i = 1
    while i < 6:
        print(i)
        i+=1 

whileLoop()

