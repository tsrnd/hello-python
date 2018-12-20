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

