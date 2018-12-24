
def countingSort(array):
    maxArray, minArray = max(array), min(array)
    arr = []
    arrayIndex = [0] * (maxArray - minArray + 1)
    for i in array:
        arrayIndex[i + abs(minArray) - 1] += 1
    for i in range(minArray, maxArray + 1):
        while arrayIndex[i + abs(minArray) - 1]:
            arrayIndex[i + abs(minArray) - 1] -= 1
            arr.append(i)
    return arr


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
