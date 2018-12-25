#!/usr/bin/python
import math


def introSort(a, d):
    n = len(a)
    if n <= 1:
        return
    elif d == 0:
        heapSort(a)
    else:
        p = partition(a)
        a1 = a[:p]
        a2 = a[p+1:n]
        introSort(a1, d-1)
        introSort(a2, d-1)
        for i in range(0, len(a1)):
            a.insert(i, a1[i])
            a.pop(i+1)
        for i in range(0, len(a2)-1):
            a.insert(i+p+1, a2[i])
            a.pop(i+p+2)
    return


def heapSort(a):
    END = len(a)
    for k in range(int(math.floor(END/2)) - 1, -1, -1):
        heapify(a, END, k)

    for k in range(END, 1, -1):
        a[0], a[k-1] = a[k-1], a[0]
        heapify(a, k-1, 0)
    return


def partition(a):
    hi = len(a)-1
    x = a[hi]
    i = 0
    for j in range(0, hi-1):
        if a[j] <= x:
            a[i], a[j] = a[j], a[i]
            i = i + 1
    a[i], a[hi] = a[hi], a[i]
    return i


def heapify(a, iEnd, iRoot):
    iL = 2*iRoot + 1
    iR = 2*iRoot + 2
    if iR < iEnd:
        if (a[iRoot] >= a[iL] and a[iRoot] >= a[iR]):
            return

        else:
            if(a[iL] > a[iR]):
                j = iL
            else:
                j = iR
            a[iRoot], a[j] = a[j], a[iRoot]
            heapify(a, iEnd, j)
    elif iL < iEnd:
        if (a[iRoot] >= a[iL]):
            return
        else:
            a[iRoot], a[iL] = a[iL], a[iRoot]
            heapify(a, iEnd, iL)

    else:
        return


# Driver program to test above function
if __name__ == "__main__":
    a = [random.uniform(-100000, 100000) for _ in range(10000)]
    b = a.copy()
    b.sort()
    print( b == introSort(a, 2))