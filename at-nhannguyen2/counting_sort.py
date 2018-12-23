def CountingSort(array):
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
