def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def mergesort(array):
    if len(array) > 1:
        mid = len(array)//2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

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
