def heapSort(array):
    length = len(array) - 1
    beginIndex = (length - 1) >> 1
    for i in range(beginIndex, -1, -1):
        maxHeapify(i, length, array)
    for i in range(length, 0, -1):
        array[0], array[i] = array[i], array[0]
        maxHeapify(0, i - 1, array)
    return array


def maxHeapify(index, length, array):
    li = (index << 1) + 1
    ri = li + 1
    cMax = li
    if li > length:
        return
    if ri <= length and array[ri] > array[li]:
        cMax = ri
    if array[cMax] > array[index]:
        array[cMax], array[index] = array[index], array[cMax]
        maxHeapify(cMax, length, array)
