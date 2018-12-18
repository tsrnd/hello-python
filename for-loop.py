numbers = [6, 5, 4, 3, -4, 3, 5, 4, -11]
for val in numbers:
    print(val)

print("=================")
for i in range(len(numbers)):
    print(numbers[i])

print("=================")
for i in range(2, len(numbers), 2):
    print(numbers[i])

print("=================")

for val in numbers:
    if val > 0:
        print(val)
    else:
        break
else:
    print("no more")

print("=================")

for val in numbers:
    if val < 0:
        continue
    print(val)
else:
    print("no more", 2)
print("=================")

str = "hello"
for i in str:
    print(i)

