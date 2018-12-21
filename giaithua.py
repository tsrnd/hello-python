def countIncreasingSequences(n, k):
    return giaithua(k)/(giaithua(n)*giaithua(k-n))
def giaithua(n):
    result = 1
    for i in range(n+1):
        if i == 0:
            continue
        result *= i
    return result
print(countIncreasingSequences(2,4))
print(range(3))
for i in range(3)
    print(i)

