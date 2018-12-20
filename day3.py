import pack1.subpack1.subsubpack1.module1 as mymodule1
import os
print('#######################################################')
# func and module
print(len(mymodule1.nCk(4,2)), len(mymodule1.nPk(4,2)), len(mymodule1.nHk(4)))
# arrange multi type in list
a = ['ss', '1',1,'ee', '22', '1', '1']
def keyFunc(x):
    v = x
    if isinstance(v, int): v = '0%d' % v
    print(v)
    return v
print(sorted(a, key= keyFunc))
# lambda func
a = ['ss', '1',1,'ee', '22', '1', '1']
print(sorted(a, key= lambda x : str(x)))

# use dict
print({key:value for key, value in zip(range(10), range(10))})
print('#######################################################')
# module
import math
math.__file__
print('module math support properties and func is: ', dir(math))
print()
print('properties and func of current scope is: ', dir())
print('#######################################################')
# File I/O
if not os.path.isdir('tmp'):
    os.mkdir('tmp')
f1 = open('tmp/myfile1.txt', 'a+')
print("Content file is: ", f1.read())
print(f1.write("first line"))
f1.seek(0)
print("Content file after is: ", f1.read())
f1.close()
# remove empty dir: os.removedirs("tmp")
# remove un-empty dir
import shutil
shutil.rmtree('tmp') 

print('#######################################################')
# Exception

lis = list()
try:
    lis.index(0)
except:
    pos = -1
else:
    pos = lis.index(0)    
finally:
    print(f"Position of 0 in list is: {pos}")
"""
print('#######################################################')
# Image
from PIL import Image
fIm = Image.open("a.jpg")
fImb = Image.open("b.jpg")
fIm.save("new_a.jpg", "JPEG")
fImb.save("new_a.jpg")
fIm.thumbnail((100,100))
"""
print('#######################################################')
# File JSON
import urllib.request, json
url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=16.0406376,108.2275175&key=AIzaSyCC4ozgNyQ29E9z-F8MwkkmxzJN6H558ys&types=country"
resp = urllib.request.urlopen(url)
# decode response to json sring follow format
fjsonstr = resp.read().decode('utf-8')
print(type(fjsonstr),"\n", fjsonstr,"\n")
# convert json sring into data
data = json.loads(fjsonstr)
print(type(data),"\n", data,"\n")
# convert data into json sring 
jsonstr = json.dumps(data)
print(type(jsonstr), "\n",jsonstr,"\n")
