# List
def sort(arr):
    return sorted(arr)

print(sort([1,3,51,23,5,3,6,8,8,4]))

def removeDuplicate(arr):
    return list(set(arr))

print(removeDuplicate([1,3,51,23,5,3,6,8,8,4]))

def checkIfSameDigit(num):
    return len(set(str(num))) == 1

print(checkIfSameDigit(112113))
print(checkIfSameDigit(111222))
print(checkIfSameDigit(11111))

def checkItemInList(item, arr):
    return item in arr

print(checkItemInList("a", [1,2,3,4,5]))
print(checkItemInList("a", ["a", "b"]))

def append():
    arr = ["1","2","3","4"]
    arr.append("2")
    print(arr)

append()

def insertAtIndex(index, int):
    arr = [2]
    arr.insert(index, int)

insertAtIndex(0,10)

def remove():
    arr = [0,1,2,3,4,5,6,7,8,9]
    arr.remove(7)
    print(arr.pop(0))

remove()

def index():
    arr = [0,1,2,3,4,5,6,7,8,9,1,9] 
    print(arr.index(4))

index()

# Dictionary
def accessDictionary():
    thisDict = {
        "name": "sonvu",
        "age": 25
    }
    # get key "name"
    print(thisDict["name"])
    print(thisDict.get("name"))

    # if key not exist will show error
    #print(thisDict["none"])

    # change value dictionary
    thisDict["age"] = 23

    # add item to dictionary
    thisDict["none"] = 25

    print(thisDict)

accessDictionary()


