def mixedFractionToImproper(a):
    return [(a[0] + a[1]/a[2]) * a[2], a[2]]
print (mixedFractionToImproper([3,1,2]))