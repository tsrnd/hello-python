def checkPrime(n):
    return len([x for x in range(1, n + 1) if n % x == 0]) == 2

def makeThisNotCoverage(n):
    if n == 1:
        return True
    else:
        return False