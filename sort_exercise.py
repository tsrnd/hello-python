def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
    return


def gnomeSort(array):
    first = 0
    while first < len(array):
        if first == 0 or (array[first-1] <= array[first]):
            first += 1
        else:
            swap(array, first, first-1)
            first -= 1
    return array


def oldEventSort(array):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, len(array)-1, 2):
            if array[i] > array[i+1]:
                swap(array, i, i+1)
                sorted = False
        for i in range(0, len(array)-1, 2):
            if array[i] > array[i+1]:
                swap(array, i, i+1)
                sorted = False
    return array
