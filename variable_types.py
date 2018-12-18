# Numbers
var1 = 1
print(var1)
del var1
if 'var1' in locals():
    print('cannot delete var1')
else:
    print('var1 is deleted')

'''
1
var1 is deleted
'''

# String
str1 = 'hello python'
print(str1)
print(str1[0])
print(str1[2:5])
print(str1[2:])

'''
hello python
h
llo
llo python
'''

# List
list1 = ['abcd', 123, 4.56, 'john', 77.3]
list2 = [123, 'john']
print(list1)
print(list1[1:3])
print(list1[2:])
print(list2 * 2)
print(list2 + list1)
'''
['abcd', 123, 4.56, 'john', 77.3]
[123, 4.56]
[4.56, 'john', 77.3]
[123, 'john', 123, 'john']
[123, 'john', 'abcd', 123, 4.56, 'john', 77.3]
'''

# Tuple
tuple1 = (1, 'abc', 345, 'def', 77.7)
tuple2 = (2, 'xyz', 7.5)
print(tuple1)
print(tuple1[0])
print(tuple1[1:3])
print(tuple1[1:])
print(tuple2 * 2)
print(tuple1 + tuple2)
'''
(1, 'abc', 345, 'def', 77.7)
1
('abc', 345)
('abc', 345, 'def', 77.7)
(2, 'xyz', 7.5, 2, 'xyz', 7.5)
(1, 'abc', 345, 'def', 77.7, 2, 'xyz', 7.5)
'''

# Dictionary
dict1 = {}
dict1['one'] = 'This is one'
dict1[2] = 'This is two'
dict2 = {'name': 'john', 'code':'123', 'dept': 'ts'}
print(dict1['one'])
print(dict1[2])
print(dict2)
print(dict2.keys())
print(dict2.values())
'''
This is one
This is two
{'name': 'john', 'code': '123', 'dept': 'ts'}
dict_keys(['name', 'code', 'dept'])
dict_values(['john', '123', 'ts'])
'''

# Conversion
msg = "print('hello')"
eval(msg)
'''
hello
'''
