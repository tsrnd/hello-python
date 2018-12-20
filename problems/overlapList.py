a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def remove_repetidos(a,b):
    c=a+b
    l=[]
    for i in c:
        if i not in l and i not in a or i not in b:
            l.append(i)
            l.sort()
    return l
print(remove_repetidos(a, b))
