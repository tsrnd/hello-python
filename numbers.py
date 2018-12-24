print('= Numbers =')

# Mathematical Functions
print('# Mathematical Functions')

from math import trunc, floor, ceil

num = 3.45
print('num =', num)
print('trunc =', trunc(num))
print('round =', round(num))
print('floor =', floor(num))
print('ceil =', ceil(num))
'''
num = 3.45
trunc = 3
round = 3
floor = 3
ceil = 4
'''

# Random Number Functions
print('# Random Number Functions')
from random import choice, shuffle, uniform

seq = ['red', 'blue', 'green', 'yellow']
print('seq =', seq)
color = choice(seq)
print('choice =', color)
shuffle(seq)
print('shuffle =', seq)
'''
seq = ['red', 'blue', 'green', 'yellow']
choice = green
shuffle = ['green', 'red', 'blue', 'yellow']
'''

print('uniform(3, 7) =', uniform(3, 7))
'''
uniform(3, 7) = 5.076150395551634
'''
