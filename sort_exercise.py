
def mergeSort(array):
    if len(array) > 1:
        mid = len(array)//2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i = i+1
            else:
                array[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            array[k] = righthalf[j]
            j = j+1
            k = k+1
        return array


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
