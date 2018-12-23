def merge(array):
    l, m, h = 0, len(array) // 2, len(array)
    l1, l2, i = l, m, l
    res = [0]*h
    while l1 < m and l2 < h:
        if array[l1] <= array[l2]:
            res[i] = array[l1]
            l1 += 1
        else:
            res[i] = array[l2]
            l2 += 1
        i += 1
    while l1 < m:
        res[i] = array[l1]
        i += 1
        l1 += 1

    while l2 < h:
        res[i] = array[l2]
        i += 1
        l2 += 1

    for i in range(l, h):
        array[i] = res[i]
    return res


def MergeSort(array):
    m = len(array) // 2
    if len(array) > 1:
        arrayA = MergeSort(array[:m])
        arrayB = MergeSort(array[m:])
        array = merge(arrayA + arrayB)
    return array
