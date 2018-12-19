# Arithmetic Operators
# Comparison (Relational) Operators
# Assignment Operators
# Logical Operators
# Bitwise Operators
# Membership Operators
num = 1
seq1 = {'1': 1}
seq2 = {1: '1'}
if num in seq1:
  print('num is in seq1')
else:
  print('num is not in seq1')
if num in seq2:
  print('num is in seq2')
else:
  print('num is not in seq2')
'''
num is not in seq1
num is in seq2
'''

# Identity Operators
a = "hello"
b = "hello"
c = "python"
if a is b:
  print("a<%s> is b<%s>" % (id(a), id(b)))
else:
  print("a<%s> is not b<%s>" % (id(a), id(b)))
if c is b:
  print("c<%s> is b<%s>" % (id(c), id(b)))
else:
  print("c<%s> is not b<%s>" % (id(c), id(b)))
