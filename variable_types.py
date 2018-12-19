counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

print (counter)
print (miles)
print (name)

# Multiple Assignment
a, b, c = 1, 2, "john"

# del statement
del a, b

# standard data types
# number
var1 = 1
var2 = 10
# string
str = 'Hello World!'

print (str)       
print (str[0])      
print (str[2:5])    
print (str[2:])      
print (str * 2) 
print (str + "TEST")
# list
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)       
print (list[0])    
print (list[1:3])   
print (list[2:]) 
print (tinylist * 2)
print (list + tinylist)
# tuple
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)         
print (tuple[0])        
print (tuple[1:3])     
print (tuple[2:])      
print (tinytuple * 2)
print (tuple + tinytuple)
# dictionary
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (dict['one'])
print (dict[2])        
print (tinydict)
print (tinydict.keys())
print (tinydict.values())