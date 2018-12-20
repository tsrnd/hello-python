def sum(a, b):
    return a + b

sum(4,5)
sum("hello", "python")

# Type 
def typeIdentification(a):
    return type(a)

typeIdentification(1)
typeIdentification(2.8)
typeIdentification("2")
typeIdentification(1j)

# Casting
def castStrToInt(str): 
    try:
        return int(str)
    except:
        print("can't not cast")

# String
def getStringByPosition(str):
    # get string by index 2 -> 5
    return str[2:5]

getStringByPosition("0123456789")

# Strip
def stripString(str):
    return str.strip()

stripString("       Hello python   ") 

# Get length of String
def lengthString(str):
    return len(str)

print(lengthString("123455"))