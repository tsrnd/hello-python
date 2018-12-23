def insertion_sort(array):
    for i in range(1, len(array)):
        current_value = array[i]
        position = i
        while position > 0 and array[position - 1] > current_value:
            array[position] = array[position - 1]
            position = position - 1

        array[position] = current_value

    return array


def selection_sort(array):
    for i in range(len(array)):
        min_position = i

        for j in range(i + 1, len(array)):
            if array[min_position] > array[j]:
                min_position = j

        temp = array[i]
        array[i] = array[min_position]
        array[min_position] = temp

    return array

