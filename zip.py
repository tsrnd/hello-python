colors = ["red", "blue", "green", "black"]
ratios = [0.2, 0.3, 0.1, 0.4]
for color, ratio in zip(colors, ratios):
    print(color, ratio)
    print(ratio)

for index, color in enumerate(colors[2:]):
    print(index, color)
for k,v in enumerate(colors):
    print(k,v)
