import unittest
def cocktailShakerSort(array):
    start = 0
    end = len(array)
    while start != end:
        for i in range(start, end - 1):
            if array[i] > array[i + 1]:
                tam = array[i]
                array[i] = array[i + 1]
                array[i + 1] = tam
        end -= 1
        if end == start:
            return array
        for i in range(0, end - start):
            j = end - i
            if array[j] < array[j - 1]:
                tam = array[j]
                array[j] = array[j - 1]
                array[j - 1] = tam
        start += 1
    return array