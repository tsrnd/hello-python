def leastFactorial(n):
    factorial = 1
    index = 1
    while factorial < n:
        index += 1
        factorial *= index
        print("in facto", factorial)
    return factorial

print(leastFactorial(5))