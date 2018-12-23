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

def quicksort(array):
    if not array:
        return []
    pivots = [x for x in array if x == array[0]]
    lesser = quicksort([x for x in array if x < array[0]])
    greater = quicksort([x for x in array if x > array[0]])

    return lesser + pivots + greater

# a =[12,4,5,6,7,3,1,15]
# print (quickSort(a))
# print (quicksort(a))


def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist


# print(bubbleSort(a))