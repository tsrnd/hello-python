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

print(mixedFractionToImproper([3, 1, 2, 4]))