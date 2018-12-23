def quickSort(array):
    lesser = []
    pivots = []
    greater = []

    if not array:
        return []

    pivots = [x for x in array if x == array[0]]
    lesser = quickSort([x for x in array if x < array[0]])
    greater = quickSort([x for x in array if x > array[0]])
    return lesser + pivots + greater


def gnomeSort(array):
    i = 0
    while i < len(array):
        if i == 0 or (array[i] >= array[i-1]):
            i += 1
        else:
            array[i], array[i-1] = array[i-1], array[i]
            i -= 1
    return array
