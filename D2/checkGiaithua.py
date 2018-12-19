def checkFactorial(n):
    i = 1
    k = 1
    if n==1 : return True
    while k<n:
        k*=i
        i+=1
        if k==n :
            return True
    return False
print(checkFactorial(120))