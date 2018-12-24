things = [["animal", "bear"], ["animal", "duck"], ["vehicle", "harley"], ["plant", "cactus"], \
          ["vehicle", "speed boat"], ["vehicle", "school bus"]]

from itertools import *
dic = {}
f = lambda x: x[0]
sort = sorted(things, key=f)

group = groupby(sorted(things, key=f), f)

for key, group in groupby(sorted(things, key=f), f):
    dic[key] = list(group)
print(dic)
