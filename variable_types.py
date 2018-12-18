var1 = 10
var2 = 20.0
print(var1+var2)
del var1
var3 = 2+1j
print(var3)

str = 'Hello World!'
print (str[2:100])
print(str * 2)
print (str + str[2:100])

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
tinylist.append(1001)
print(list+tinylist[3:tinylist.__len__()])
print(list+tinylist[3:100])
print(list.__len__())

tuple = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinytuple = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
tuple.append(1234)
print(tuple+tinytuple[3:tinytuple.__len__()])
print(tuple+tinytuple[3:100])
print(tuple.__len__())

dict = {}
dict["10"] = 100
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print(dict["10"])
print(tinydict.keys())
