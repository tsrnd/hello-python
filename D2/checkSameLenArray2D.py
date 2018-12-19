def areIsomorphic(array1, array2) :
    i = 0
    if (len(array1) != len(array2)) : return False
    while i < len(array1):
        if (len(array1[i]) != len(array2[i])): return False
        i+=1
    else: return True
a = [[1,1,1], [0,0]]
b = [[2,1,1], [2,1]]
print(areIsomorphic(a,b))