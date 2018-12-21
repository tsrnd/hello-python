print('= Numbers =')

# Mathematical Functions
print('# Mathematical Functions')

from math import trunc, floor, ceil

num = 3.45
print('num = %d' % num)
print('trunc = %f' % trunc(num))
print('round = %f' % round(num))
print('floor = %f' % floor(num))
print('ceil = %f' % ceil(num))
'''
num = 3
trunc = 3.000000
round = 3.000000
floor = 3.000000
ceil = 4.000000
'''

# Random Number Functions
print('# Random Number Functions')
from random import choice, shuffle, uniform

seq = ['red', 'blue', 'green', 'yellow']
print('seq = ' + ', '.join(seq))
color = choice(seq)
print('choice = ' + color)
shuffle(seq)
print('shuffle = ' + ', '.join(seq))
'''
seq = red, blue, green, yellow
choice = green
shuffle = yellow, red, green, blue
'''

x = 3
y = 7
print('uniform(%d, %d) = %f' % (x, y, uniform(x, y)))
'''
uniform(3, 7) = 6.966907
'''
