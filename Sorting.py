def insertSort(array):
    i = 1
    while i < len(array):
        j = i
        while j > 0 and array[j-1] > array[j]:
            array[j], array[j-1] = array[j-1], array[j]
            j = j-1
        i = i+1
    return array


def bubleSort(array):
    i = 0
    isHasSwap = False
    while i < len(array)-1 or isHasSwap == True:
        if(i == len(array)-1):
            i = 0
            isHasSwap = False
        if(array[i+1] < array[i]):
            isHasSwap = True
            array[i], array[i+1] = array[i+1], array[i]
        else:
            i = i+1
    return array
