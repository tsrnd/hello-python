import math

def fib(n):
   result = []
   a, b = 0, 1
   while b < n:
      result.append(b)
      a, b = b, a + b
   return result
# >>> from fib import fib
print(fib(100))
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print (math.ceil(3.2))
print (math.floor(3.2))

from math import ceil
print (ceil(2.3))

from math import *
print (factorial(5))

import mathPlus
print (mathPlus.mathSum(2,3))

from mathPlus import mathSum
print (mathSum(3,4))

import mathPlus as mathSPlus
print (mathSPlus.mathSum(3,5))

from mathPlus import *
print (mathPlus._math_tru(4,1))

import os, sys
lib_path = os.path.abspath(os.path.join('modules'))
sys.path.append(lib_path)
from differenceFolder import giaiThua
giaiThua(4)


import math

content = dir(math)
print (content)