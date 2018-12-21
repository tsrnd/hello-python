from itertools import combinations
def countIncreasingSequences(n, k):
    perm = combinations(list(range(1, k + 1)), n)
    return len(list(perm))
print(countIncreasingSequences(2,4))
