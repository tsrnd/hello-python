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


def countingSort(array):
    maxArray, minArray = max(array), min(array)
    res = []
    listIndex = [0] * (maxArray - minArray + 1)
    for i in array:
        listIndex[i + abs(minArray) - 1] += 1
    for i in range(minArray, maxArray + 1):
        while listIndex[i + abs(minArray) - 1]:
            listIndex[i + abs(minArray) - 1] -= 1
            res.append(i)
    return res
