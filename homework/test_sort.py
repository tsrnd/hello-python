from main import *
import random

def randomInputArray():
    array = []
    for _ in range(9999):
        array.append(random.randint(-100000, 100000))
    return array

def test_quick_sort():
    for _ in range(100):
        array = randomInputArray()
        sorted_list = sorted(array)
        assert(sorted_list == quickSort(array))

def test_shell_sort():
    for _ in range(100):
        array = randomInputArray()
        sorted_list = sorted(array)
        assert(sorted_list == shellSort(array))