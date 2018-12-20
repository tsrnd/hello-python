for i in list(range(5)):
    print(i)
number = [2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in number:
    if i % 2 == 0:
        print("So chan la :", i)
else:
    print('khong co so chan')
var = 0
while var < 5:
    print(var, "nho hon 5")
    var = var + 1
else:
    print(var, "khong nho hon 5")

for i in range(1, 10):
    for j in range(1, 10):
        k = i * j
        print(k, end=' ')
    print()
