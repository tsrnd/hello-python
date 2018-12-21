from sorting import *
import random


def randomInputArray():
    array = []
    for _ in range(9999):
        array.append(random.randint(-100000, 100000))
    return array


def test_quick_sort():
    a = randomInputArray()
    b = sorted(a)
    assert b == quickSort(a)


def test_heap_sort():
    a = randomInputArray()
    b = sorted(a)
    assert b == heapSort(a)
