def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def insertionsort(array):
    for index in range(1, len(array)):
        current_value = array[index]
        position = index

        while position > 0 and array[position-1] > current_value:
            array[position] = array[position-1]
            position = position-1
        array[position] = current_value
    return array
