def insertionSort(a):
    for i in range(1, len(a)):
        t = a[i]
        index = i
        for j in range(i -1, -1, -1):  
            if a[j] > t:
                a[j + 1] = a[j]
                index = j
            else:
                break
        if index != i:
            a[index] = t
    return a

# a = [3, 6, 9, 2, 6, 8, 9, 1, 7, 21, 7, 12]
# x = insertionSort(a)
# print(x)
# result is: [1, 2, 3, 6, 6, 7, 7, 8, 9, 9, 12, 21]
