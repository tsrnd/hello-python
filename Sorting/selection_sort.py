def swap(list, i, j):
    temp = list[i]
    list[i] =  list[j]
    list[j] = temp
    return

def selection_sort(list):
    for i in range(0, len(list) - 1, 1):
        iMin = i
        for ii in range(i +1, len(list) - 1, 1):
            if list[i] > list[ii]:
                iMin = ii
        if iMin != i:
            swap(list, i, iMin)
    return

