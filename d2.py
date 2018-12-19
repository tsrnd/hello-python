import time

cars = ["Ford", "Volvo", "BMW"]
cars.pop(0)
print(cars)

# a = b = c = 1
a, b, c = 1, 2, "john"
print(a, b, c)

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print (tinylist * 2)
print (list + tinylist)

d = {
    "aa": "bb",
    "bb": "cc"
}
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print (d)
print (dict['one'])
print (dict[2])
print (tinydict)
print (tinydict.keys())
print (tinydict.values())

tup = ('physics', 'chemistry', 1997, 2000)

print (tup)
del tup
# print ("After deleting tup : ")
# print (tup)

localtime = time.asctime( time.localtime(time.time()) )
time = time.localtime(time.time())
print (time)
print ("time: ", localtime)
