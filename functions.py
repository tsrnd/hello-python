print('= Functions =')

def split(s, l = 0, r = None):
  if r == None:
    r = len(s)
  return s[l:r]

print("split('abcdef', 2, 4) =", split('abcdef', 2, 4))
'''
split('abcdef', 2, 4) = cd
'''

print("split('abcdef', r = -2) =", split('abcdef', r = -2))
'''
split('abcdef', r = -2) = abcd
'''

print("split('abcdef', -2) =", split('abcdef', -2))
'''
split('abcdef', -2) = ef
'''

# Lambda
print('# Lambda')

block = lambda a, b: a + b
print(block(1, 2))
