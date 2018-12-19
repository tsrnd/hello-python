colors = ["red", "blue", "green", "black"]
ratios = [0.2, 0.3, 0.1, 0.4]
for color, ratio in zip(colors, ratios):
    print(color, ratio)
    print(ratio)

for index, color in enumerate(colors[2:]):
    print(index, color)

for k,v in enumerate(colors):
    print(k,v)

for x in range(6):
    print(x)

tup1 = tuple(colors)
print(tup1)
tup2 = (1, ["test", "testing"], "hi")
print(tup2)
tup2[1][0] = 3
print(tup2)

lamb = lambda x:x**2
print(lamb(5))

car = {
    "brand": "Ford"
}
print(car, car.get("brand"))
car["brand"] = "Toyota"
print(car.get("brand"))
car.clear()
print(car)

aters = {"hung", "hungdaihiep", "daihiephung", "Hung"}
for ater in aters:
    print(ater)
if "hung" in aters:
    print("welcome")
aters.add("sep")
print(aters)
aters.remove("sep")
print(aters)
aters.discard("sep")
print(aters)
