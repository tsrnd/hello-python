print("Hello Control Structure")

a = 1
b = 2
c = 5
print("If else :")
if a < b:
    print(a, "<", b)
elif a < c:
    print(a, "<", c)
else:
    print("end")

print("For :")
array = ["Monday", "Tueday", "Sunday"]
for i in array:
    print(i)

print("For with index:")
array = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
for index in range(len(array)):
    print("Index: ", index, " = ", array[index])

count = 0
print("While :")
while(count <= 10):
    print("Count= ", count)
    count = count+1

print("Good Bye! ")
