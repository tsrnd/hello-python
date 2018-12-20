import os

def invert_dict(d):
    inv = dict()
    for key in d:
        value = d[key]
        if key not in inv:
           inv[value] = [key]
        else:
           inv[value].append(key)
    return inv
print(invert_dict({'a': 1, 'b': 1, 'c': 2, 'd': 3, 'e': 2}))

def checkIfSameDigit(num):
   return len(set(str(num))) == 1
print(checkIfSameDigit(1111))

print('I have %d girls friend in %d years' %(3, 2))
print(os.getcwd())
print(os.path.abspath('output.txt'))