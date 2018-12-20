def replaceFirstDigitRegExp(input):
    for i in range(0, len(input)):
        if input[i].isdigit():
            return input[:i] + "#" + input[i + 1:]
print(replaceFirstDigitRegExp("There are 12 points"))

def countIncreasingSequences(n, k):
    tong = 0
    if n > k:
        return 0
    elif n == k:
        return 1
    else:
        so = k - n + 1
        for i in range(0, k - n + 1):
            tong = tong + so
            so -= 1
        return tong

print(countIncreasingSequences(2, 3)) 

def countIncreasingSequences(n, k):
    kk = k
    tong = 0
    buoc = k - n
    for i in range(0, n):
        tong = tong + k
        k -= buoc
    return tong
print(countIncreasingSequences(2,3))
