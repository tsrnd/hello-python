
def selectSort(array):
    for i in range(len(array)-1):
        indexMin = i
        for j in range(i+1, len(array)):
            if array[j] < array[indexMin]:
                indexMin = j
        array[i], array[indexMin] = array[indexMin], array[i]
    return array


def oldEventSort(array):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, len(array)-1, 2):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                sorted = False
        for i in range(0, len(array)-1, 2):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                sorted = False
    return array
