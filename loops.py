# while loop
a = 6
while a > 0:
    a -= 1
    if a == 4:
        continue
    if a == 1:
        break
    print(a)
# result
# 5
# 3
# 2

#############
d = ['a', 'b', 'c']
while d:
    print(d.pop(-1))
    # result
    # c
    # b
    # a

# for loop

arr = ["1", "2", "3", "4"]
for value in arr:
    print(value)
#########

n = 6
arr1 = []
for v in range(1, n+1):
    arr1.append(v)
print(arr1)

# nested loops
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
k = 1
for i in range(0, 3):
    k *= 10
    for j in range(0, 3):
        A[i][j] *= k
        if A[i][j] >= 700:
            break
print(A)
