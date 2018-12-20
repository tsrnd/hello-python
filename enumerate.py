#enumerate
presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
for i in range(len(presidents)):
    print("in i ", i)
    print("President {}: {}".format(i + 1, presidents[i]))
    print("format", format(i+1))


presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
for num, name in enumerate(presidents, start=1):
    print("nums",num)
    print("name",name)
    print("President {}: {}".format(num, name))

colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
# print("a",ratios)
for i, color in enumerate(colors):
    ratio = ratios[i]
    print("in i ", i)
    print("ratio", ratio)
    print("{}% {}".format(ratio * 100, color))

zip
colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
for color, ratio in zip(colors, ratios):
    print("{}% {}".format(ratio * 100, color))

alist = ['a1', 'a2', 'a3']
for i, a in enumerate(alist):
    print(i, a)