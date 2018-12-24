###quick sort
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
        return quickSort(less)+equal+quickSort(greater)
    else:
        return array


###shell sort
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

###bubble sort
def bubbleSort(arr):
    for passnum in range(len(arr)-1,0,-1):
        for i in range(passnum):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr

###insertion sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        t = arr[i]
        index = i
        for j in range(i -1, -1, -1):  
            if arr[j] > t:
                arr[j + 1] = arr[j]
                index = j
            else:
                break
        if index != i:
            arr[index] = t
    return arr