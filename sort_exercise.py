
def selectSort(array):
    for i in range(len(array)-1):
        indexMin = i
        for j in range(i+1, len(array)):
            if array[j] < array[indexMin]:
                indexMin = j
        array[i], array[indexMin] = array[indexMin], array[i]
    return array


def quickSort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quickSort(less) + equal + quickSort(greater)
    else:
        return array
