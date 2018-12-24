print('= Variable Types =')

# Numbers
print('# Numbers')

var1 = 1
print('var1 =', var1)
del var1
if 'var1' in locals():
    print('cannot delete var1')
else:
    print('var1 is deleted')
'''
var1 = 1
var1 is deleted
'''

# String
print('# String')

str1 = 'hello python'
print('str1 =', str1)
print('str1[0] =', str1[0])
print('str1[2:5] =', str1[2:5])
print('str1[2:] =', str1[2:])
'''
str1 = hello python
str1[0] = h
str1[2:5] = llo
str1[2:] = llo python
'''

# List
print('# List')

list1 = ['abcd', 123, 4.56, 'john', 77.3]
list2 = [123, 'john']
print('list1 =', list1)
print('list1[1:3] =', list1[1:3])
print('list1[2:] =', list1[2:])
print('list2 * 2 =', list2 * 2)
print('list2 + list1 =', list2 + list1)
'''
list1 = ['abcd', 123, 4.56, 'john', 77.3]
list1[1:3] = [123, 4.56]
list1[2:] = [4.56, 'john', 77.3]
list2 * 2 = [123, 'john', 123, 'john']
list2 + list1 = [123, 'john', 'abcd', 123, 4.56, 'john', 77.3]
'''

# Tuple
print('# Tuple')

tuple1 = (1, 'abc', 345, 'def', 77.7)
tuple2 = (2, 'xyz', 7.5)
print('tuple1 =', tuple1)
print('tuple1[0] =', tuple1[0])
print('tuple1[1:3] =', tuple1[1:3])
print('tuple1[1:] =', tuple1[1:])
print('tuple2 * 2 =', tuple2 * 2)
print('tuple1 + tuple2 =', tuple1 + tuple2)
'''
tuple1 = (1, 'abc', 345, 'def', 77.7)
tuple1[0] = 1
tuple1[1:3] = ('abc', 345)
tuple1[1:] = ('abc', 345, 'def', 77.7)
tuple2 * 2 = (2, 'xyz', 7.5, 2, 'xyz', 7.5)
tuple1 + tuple2 = (1, 'abc', 345, 'def', 77.7, 2, 'xyz', 7.5)
'''

# Dictionary
print('# Dictionary')

dict1 = {}
dict1['one'] = 'This is one'
dict1[2] = 'This is two'
dict2 = {'name': 'john', 'code':'123', 'dept': 'ts'}
print('dict1 =', dict1)
print("dict1['one'] =", dict1['one'])
print('dict1[2] =', dict1[2])
print('dict2 =', dict2)
print('dict1.keys() =', dict2.keys())
print('dict2.values() =', dict2.values())
'''
dict1 = {'one': 'This is one', 2: 'This is two'}
dict1['one'] = This is one
dict1[2] = This is two
dict2 = {'name': 'john', 'code': '123', 'dept': 'ts'}
dict1.keys() = dict_keys(['name', 'code', 'dept'])
dict2.values() = dict_values(['john', '123', 'ts'])
'''

# Conversion
print('# Conversion')

msg = "print('hello')"
print('evaluating', msg)
eval(msg)
'''
evaluating print('hello')
hello
'''

msg = "print(1+2*3)"
print('evaluating', msg)
eval(msg)
'''
evaluating print(1+2*3)
7
'''
