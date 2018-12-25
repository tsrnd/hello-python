def quicksort(array):
    less = []
    pivots = []
    greater = []
    if not array:
        return []
    pivots = [x for x in array if x == array[0]]
    less = quicksort([x for x in array if x < array[0]])
    greater = quicksort([x for x in array if x > array[0]])
    return less + pivots + greater

#a = [3, 6, 9, 2, 6, 8, 9, 1, 7, 21, 7, 12]

#x = quicksort(a)

#print("After sorting: ", x)
# result is: 'After sorting:  [1, 2, 3, 6, 6, 7, 7, 8, 9, 9, 12, 21]'
