def sum(a,b) :
    return a + b
print(sum(2,3))

def changeElement(listChange):
    print ('List before change : ', listChange )
    listChange[0] = 'changed'
    print ('List after change : ', listChange)
    return
list = [1,2,3]
changeElement(list)
print('List after use function: ', list)

def printStr(string):
    print(string)
printStr("Nothing's gonna change my love for u")

def yourInfo(name, age= 22):
    print ('Your name is: ', name)
    print ('Your age is: ', age)
    return
yourInfo('Lee.Wuan.Jain')
yourInfo('Next year', 23)

def moreParam(x, *y):
    print(x)
    for i in y:
        print (i, end=' ')
    return
moreParam(10)
moreParam(12,123,412,23)

print('\n')
def swap(a,b):
    temp = a
    a=b
    b=temp
    print (a, b)
changeLocation = lambda x, y: swap(x,y)
changeLocation(12,45)

total = 0
def sum(a,b):
    return a+b

print ('Total is: ', sum(2,5))
print (total)