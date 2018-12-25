# Find The Highest Common Factor (HCF), also called gcd

def hcfnaive(a,b):
    if b == 0:
        return a
    else:
        return hcfnaive(b, a%b)

a = 60
b = 48

print('The gcd of %d and %d is: ' % (a,b), end='')
print(hcfnaive(a,b))

# use Loop

def computeGCD(x,y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if x % i == 0 and y % i == 0:
            gcd = i
    return gcd

a = 60
b = 48

print('The gcd of %d and %d is: ' % (a,b), end='')
print(computeGCD(a,b))
