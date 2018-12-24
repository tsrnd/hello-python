def sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)

        sort(array, low, pi-1)
        sort(array, pi+1, high)

    return array

def partition(array, low, high):
    pv = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pv:
            i += 1
            array[i], array[j] = array[j], array[i]
    
    array[i+1], array[high] = array[high], array[i+1]
    return i+1
