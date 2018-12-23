def insertion_sort(array):
    for i in range(1, len(array)):
        current_value = array[i]
        position = i
        while position > 0 and array[position - 1] > current_value:
            array[position] = array[position - 1]
            position = position - 1

        array[position] = current_value

    return array


# array = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# insertion_sort(array)
# print(array)
