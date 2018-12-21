def getMiddle(array, low, high):
    tmp = array[low]
    while low < high:
        while low < high and array[high] >= tmp:
            high -= 1
        array[low] = array[high]
        while low < high and array[low] <= tmp:
            low += 1
        array[high] = array[low]
    array[low] = tmp
    return low


def sorting(array, low, high):
    if low < high:
        middle = getMiddle(array, low, high)
        sorting(array, low, middle - 1)
        sorting(array, middle + 1, high)


def quickSort(array):
    sorting(array, 0, len(array) - 1)
    return array
