def get_insertion_sort(array):
    for i in range(1, len(array)):
        currentvalue = array[i]
        position = i
        while position > 0 and array[position - 1] > currentvalue:
            array[position] = array[position - 1]
            position = position - 1
        array[position] = currentvalue
    return array

# x = get_insertion_sort([1, 3, 4, 2, 5, 7, 6])
# print(x)
# result is: [1, 2, 3, 4, 5, 6, 7]
