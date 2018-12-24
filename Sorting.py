def insertSort(array):
    i = 1
    while i < len(array):
        marker = array[i]
        j = i
        while j > 0 and array[j-1] > marker:
            array[j] = array[j-1]
            j = j-1
        i = i+1
        array[j] = marker
    return array


def bubleSort(array):
    i = 0
    isHasSwap = False
    n = len(array)-1
    while i < n or isHasSwap == True:
        if(i == n):
            i = 0
            isHasSwap = False
            n = n-1
        elif(array[i+1] < array[i]):
            isHasSwap = True
            array[i], array[i+1] = array[i+1], array[i]
        else:
            i = i+1
    return array
