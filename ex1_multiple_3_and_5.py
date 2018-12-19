# Find the sum of all the multiples of 3 or 5 below 1000.
n = 1000

sum = 0
for i in range(0,n):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print(sum)
