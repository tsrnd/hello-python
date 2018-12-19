def mixedFractionToImproper(a):
    mixValue = []
    lenA = len(a)
    print(lenA)
    if lenA <=2:
        return a;
    
    
    mixValue.append(a[0]*a[2] + a[1])
    mixValue.append(a[2])

    for ch in range(3, len(a)):
        mixValue.append(a[ch])
    print(mixValue)
    
    return mixedFractionToImproper(mixValue);

#print(mixedFractionToImproper([3, 1, 2, 4]))
def isPermutation(n, inputArray):
    if len(inputArray) <=1: return False;

    if checkSequense(inputArray): return True;

    for i in range(0, n-1):
        if inputArray[i] > inputArray[i + 1]:
            tmpArray = inputArray.copy()
            tmpArray[i] = inputArray[i+1]
            tmpArray[i+1] = inputArray[i]
            
            if checkSequense(tmpArray): return True;
            
    return False;

def checkSequense(inputArray):
    for i in range(0,len(inputArray) - 1):
        if inputArray[i] != inputArray[i+1] - 1:
            return False;
    else: return True;

print(isPermutation(2, [2, 0]))