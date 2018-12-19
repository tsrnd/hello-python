tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
smallTuple = (123, 'john')

print (tuple)     
print (tuple[0] + ' ' + tuple[3]) 
print (tuple[4] - tuple[2])  
print (tuple[1:3])   
print (tuple[2:])      
print (smallTuple * 2) 
print (tuple + smallTuple)

# tuple is a `list cứng` can not add or append new element
# tuple.append('a')
# tuple.insert(2)
print (tuple)

dictionary = {'a': 'yesterday', 'b': 'once more'}
dictionary['one'] = "This is one"
dictionary[2]     = "This is two"

smallDict = {'name': 'john','code':6734, 'dept': 'sales'}
print (dictionary)
print (dictionary['one']) 
print (dictionary[2])     
print (smallDict)       
print (smallDict.keys()) 
print (smallDict.values())

# del smallDict

dictOfWords = {
    "hello": 56,
    "at" : 23 ,
    "test" : 43,
    "this" : 97,
    "here" : 43,
    "now" : 97
    }
def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys

print(getKeysByValue(dictOfWords, 43))
for i in getKeysByValue(dictOfWords, 97):
    print (i)