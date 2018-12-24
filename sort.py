def insertionSort(inputArray):
    for x in range (1, len(inputArray)):
        a = inputArray[x]
        i = x
        while i > 0 and inputArray[i - 1] > a:
            inputArray[i] = inputArray[i - 1]
            i = i - 1
        inputArray[i] = a
    return inputArray

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
