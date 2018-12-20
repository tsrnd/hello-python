numbers = [6, 5, 4, 3, -4, 3, 5, 4, -11]
for val in numbers:
    print(val)

for i in range(len(numbers)):
    print(numbers[i])

for i in range(2, len(numbers), 2):
    print(numbers[i])


for val in numbers:
    if val > 0:
        print(val)
    else:
        break
else:
    print("no more")


for val in numbers:
    if val < 0:
        continue
    print(val)
else:
    print("no more", 2)

str = "hello"
for i in str:
    print(i)

l1 = ["eat", "sleep", "repeat", "eat"]
for count, el in enumerate(l1, 1):
    print(count, el)
