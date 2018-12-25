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

# print (countingSort(a))

def counting_sort(array, maxval):
    n = len(array)
    m = maxval + 1
    count = [0] * m               # init with zeros
    for a in array:
        count[a] += 1             # count occurences
    i = 0
    for a in range(m):            # emit
        for c in range(count[a]): # - emit 'count[a]' copies of 'a'
            array[i] = a
            i += 1
    return array

# print(counting_sort( [1, 4, 7, 2, 1, 3, 2, 1, 4, 2, 3, 2, 1], 7 ))

def shellSort(arr): 
    n = len(arr) 
    gap = n//2
    while gap > 0: 
        for i in range(gap,n): 
            temp = arr[i] 
            j = i 
            while  j >= gap and arr[j-gap] >temp: 
                arr[j] = arr[j-gap] 
                j -= gap 
            arr[j] = temp 
        gap //= 2
    return arr

# print (shellSort([1, 4, 7, 2, 1, 3, 2, 1, 4, 2, 3, 2, 1]))