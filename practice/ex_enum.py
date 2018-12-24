from enum import Enum

class Color(Enum):
    red = 1
    green = 2
    blue = 3
print(Color.red)

res = [c for c in Color if c != Color.red]
print(res)
print(8**(1/3))

from array import *
my_array = array('i', [1,2,3,4,5]) 
print(my_array.index(5))

foo = (1, 2, 3)
print(hash(foo))