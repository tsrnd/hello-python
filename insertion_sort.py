def sort(array):
    for i in range(len(array)):
        for j in range(i, 0, -1):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1] 
    
# insertionSort([1, 3, 5, 2, 4])